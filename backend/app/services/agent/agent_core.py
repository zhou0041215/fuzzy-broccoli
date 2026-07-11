"""Agent 核心 — 自主决策、多步推理、自动纠错。"""

from __future__ import annotations

import json
import logging
from typing import Any, Literal

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage
from langgraph.prebuilt import create_react_agent

from app.services.agent.models import get_llm_by_role
from app.services.agent.tools import (
    append_resume_item,
    analyze_job_description,
    create_version_snapshot,
    get_resume_summary,
    match_resume_jd,
    read_resume,
    update_resume_section,
    validate_resume,
)

logger = logging.getLogger(__name__)

# Agent 可用的工具
AGENT_TOOLS = [
    read_resume,
    update_resume_section,
    append_resume_item,
    analyze_job_description,
    match_resume_jd,
    validate_resume,
    create_version_snapshot,
    get_resume_summary,
]

# 工具名称映射
TOOL_MAP = {tool.name: tool for tool in AGENT_TOOLS}

AGENT_SYSTEM_PROMPT = """你是 FlowCV 的智能简历 Agent，具有自主决策和多步推理能力。

## 你的能力
- 读取和修改简历各个模块
- 分析岗位 JD 并计算匹配度
- 检查简历完整性和质量
- 创建版本快照保护数据安全
- 多步推理完成复杂任务

## 工作流程
1. **理解任务**：分析用户需求，确定要做什么
2. **制定计划**：列出需要执行的步骤
3. **逐步执行**：调用工具完成每个步骤
4. **验证结果**：检查执行结果是否正确
5. **自动纠错**：如果发现问题，自动修复

## 决策原则
- 先读取再修改，避免覆盖用户数据
- 重大修改前先创建快照
- 每个步骤完成后验证结果
- 如果工具调用失败，尝试其他方法
- 保持简历数据的完整性和一致性

## 回复风格
- 用中文回复
- 简洁明了，不啰嗦
- 列出执行的步骤和结果
- 如果有问题，说明原因和建议
"""


class AgentState:
    """Agent 状态管理。"""

    def __init__(self, resume_id: int | None = None):
        self.resume_id = resume_id
        self.messages: list = []
        self.tool_calls: list[dict] = []
        self.steps: list[str] = []
        self.errors: list[str] = []

    def add_message(self, role: str, content: str):
        if role == "user":
            self.messages.append(HumanMessage(content=content))
        elif role == "assistant":
            self.messages.append(AIMessage(content=content))
        elif role == "system":
            self.messages.append(SystemMessage(content=content))

    def add_tool_call(self, tool_name: str, args: dict, result: str):
        self.tool_calls.append({
            "tool": tool_name,
            "args": args,
            "result": result[:500],  # 限制长度
        })

    def add_step(self, step: str):
        self.steps.append(step)

    def add_error(self, error: str):
        self.errors.append(error)


def build_agent():
    """构建 Agent。"""
    llm = get_llm_by_role("main")
    return create_react_agent(
        llm,
        AGENT_TOOLS,
        prompt=AGENT_SYSTEM_PROMPT,
    )


def run_agent(
    user_message: str,
    resume_id: int | None = None,
    history: list[dict[str, str]] | None = None,
    *,
    max_iterations: int = 15,
) -> dict[str, Any]:
    """运行 Agent 并返回结果。

    Args:
        user_message: 用户消息
        resume_id: 当前简历 ID
        history: 对话历史
        max_iterations: 最大迭代次数

    Returns:
        {
            "reply": "AI 回复文本",
            "steps": ["步骤1", "步骤2", ...],
            "tool_calls": [{"tool": "xxx", "args": {...}, "result": "..."}],
            "resume_modified": bool,
            "errors": ["错误1", ...],
        }
    """
    agent = build_agent()
    state = AgentState(resume_id)

    # 添加简历上下文
    if resume_id:
        state.add_message("system", f"用户当前正在编辑简历 ID: {resume_id}。如果需要读取或修改简历，请使用这个 ID。")

    # 添加历史对话
    if history:
        for msg in history[-10:]:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            if role == "user":
                state.add_message("user", content)
            elif role == "assistant":
                state.add_message("assistant", content)

    # 添加当前用户消息
    state.add_message("user", user_message)

    # 运行 Agent
    resume_modified = False

    try:
        result = agent.invoke({"messages": state.messages})

        # 处理结果
        for msg in result.get("messages", []):
            # 记录工具调用
            if hasattr(msg, "tool_calls") and msg.tool_calls:
                for tc in msg.tool_calls:
                    state.add_tool_call(
                        tc.get("name", ""),
                        tc.get("args", {}),
                        "",  # 结果会在 ToolMessage 中
                    )
                    state.add_step(f"调用工具: {tc.get('name', '')}")

            # 记录工具结果
            if isinstance(msg, ToolMessage):
                content = msg.content
                # 更新最后一个工具调用的结果
                for tc in reversed(state.tool_calls):
                    if not tc["result"]:
                        tc["result"] = content[:500]
                        break

                # 检查是否修改了简历
                if any(kw in content for kw in ["成功更新", "成功向", "成功创建版本"]):
                    resume_modified = True
                    state.add_step("简历已修改")

            # 记录 Agent 思考
            if isinstance(msg, AIMessage) and msg.content:
                # 检查是否有思考过程
                if "思考" in msg.content or "计划" in msg.content:
                    state.add_step("Agent 思考中...")

        # 提取最终回复
        last_message = result["messages"][-1]
        reply = last_message.content if hasattr(last_message, "content") else str(last_message)

        return {
            "reply": reply,
            "steps": state.steps,
            "tool_calls": state.tool_calls,
            "resume_modified": resume_modified,
            "errors": state.errors,
        }

    except Exception as e:
        logger.error("Agent 执行失败: %s", e, exc_info=True)
        state.add_error(str(e))
        return {
            "reply": f"抱歉，处理过程中出现了问题：{e}",
            "steps": state.steps,
            "tool_calls": state.tool_calls,
            "resume_modified": False,
            "errors": state.errors,
        }


def run_multi_step_task(
    task_type: str,
    resume_id: int,
    params: dict[str, Any],
) -> dict[str, Any]:
    """运行多步任务。

    Args:
        task_type: 任务类型（generate, optimize, diagnose, translate）
        resume_id: 简历 ID
        params: 任务参数

    Returns:
        任务执行结果
    """
    # 根据任务类型构建提示
    prompts = {
        "generate": f"""请根据以下信息生成简历内容：
- 目标岗位：{params.get('position', '')}
- 工作经历：{params.get('work_experience', '')}
- 项目经历：{params.get('project_experience', '')}
- 教育背景：{params.get('education', '')}
- 技能：{params.get('skills', '')}

请先读取当前简历，然后生成合适的内容并写入。""",
        "optimize": f"""请优化简历内容：
- 优化目标：{params.get('target', '整体优化')}
- 目标岗位：{params.get('position', '')}
- JD：{params.get('jd', '')}

请先读取简历，然后逐步优化各个模块。""",
        "diagnose": """请诊断简历问题：
1. 读取简历内容
2. 检查完整性
3. 分析问题
4. 提供改进建议

请详细列出发现的问题和建议。""",
        "translate": f"""请翻译简历：
- 目标语言：{params.get('target_language', 'en')}

请先读取简历，然后翻译各个模块。""",
    }

    prompt = prompts.get(task_type, f"请完成以下任务：{task_type}")

    return run_agent(
        user_message=prompt,
        resume_id=resume_id,
    )
