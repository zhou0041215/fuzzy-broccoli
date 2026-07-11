"""知识库 — 存储公司、职位、技能、项目模板等结构化数据。"""

from __future__ import annotations

from typing import Any

# ============ 公司知识库 ============

COMPANY_DB: dict[str, dict[str, Any]] = {
    # 大厂
    "腾讯": {"tags": ["大厂", "互联网", "社交", "游戏"], "level": "top"},
    "阿里巴巴": {"tags": ["大厂", "电商", "云计算", "金融"], "level": "top"},
    "字节跳动": {"tags": ["大厂", "短视频", "信息流", "教育"], "level": "top"},
    "百度": {"tags": ["大厂", "搜索", "AI", "自动驾驶"], "level": "top"},
    "美团": {"tags": ["大厂", "本地生活", "外卖", "酒旅"], "level": "top"},
    "京东": {"tags": ["大厂", "电商", "物流", "金融"], "level": "top"},
    "华为": {"tags": ["大厂", "通信", "芯片", "云计算"], "level": "top"},
    "小米": {"tags": ["大厂", "硬件", "IoT", "手机"], "level": "top"},
    "网易": {"tags": ["大厂", "游戏", "音乐", "教育"], "level": "top"},
    "快手": {"tags": ["大厂", "短视频", "直播", "电商"], "level": "top"},
    # 金融
    "蚂蚁集团": {"tags": ["金融", "支付", "区块链"], "level": "top"},
    "招商银行": {"tags": ["银行", "金融"], "level": "high"},
    "中信证券": {"tags": ["证券", "金融"], "level": "high"},
    # 外企
    "微软": {"tags": ["外企", "云计算", "AI", "办公"], "level": "top"},
    "谷歌": {"tags": ["外企", "搜索", "AI", "云计算"], "level": "top"},
    "苹果": {"tags": ["外企", "硬件", "生态"], "level": "top"},
    "亚马逊": {"tags": ["外企", "电商", "云计算"], "level": "top"},
}

# ============ 职位知识库 ============

POSITION_DB: dict[str, dict[str, Any]] = {
    # 技术
    "后端开发": {
        "skills": ["Java", "Python", "Go", "MySQL", "Redis", "微服务", "分布式", "Docker"],
        "keywords": ["接口开发", "系统设计", "性能优化", "高并发"],
    },
    "前端开发": {
        "skills": ["Vue", "React", "TypeScript", "JavaScript", "HTML/CSS", "Webpack", "Node.js"],
        "keywords": ["组件开发", "响应式", "性能优化", "用户体验"],
    },
    "全栈开发": {
        "skills": ["Vue/React", "Node.js", "Python/Java", "MySQL", "MongoDB", "Docker"],
        "keywords": ["全链路开发", "架构设计", "技术选型"],
    },
    "算法工程师": {
        "skills": ["Python", "PyTorch", "TensorFlow", "机器学习", "深度学习", "NLP", "CV"],
        "keywords": ["模型训练", "特征工程", "数据处理", "算法优化"],
    },
    "数据分析师": {
        "skills": ["SQL", "Python", "Excel", "Tableau", "PowerBI", "数据可视化"],
        "keywords": ["数据清洗", "指标分析", "用户画像", "A/B测试"],
    },
    "产品经理": {
        "skills": ["需求分析", "竞品分析", "用户研究", "Axure", "Figma", "数据分析"],
        "keywords": ["产品规划", "功能设计", "项目推进", "用户增长"],
    },
    "UI设计师": {
        "skills": ["Figma", "Sketch", "Photoshop", "Illustrator", "交互设计", "视觉设计"],
        "keywords": ["界面设计", "设计规范", "用户体验", "品牌设计"],
    },
    "运营": {
        "skills": ["内容运营", "用户运营", "活动策划", "数据分析", "新媒体"],
        "keywords": ["用户增长", "留存提升", "内容策划", "社群管理"],
    },
    "测试": {
        "skills": ["功能测试", "自动化测试", "性能测试", "Selenium", "JMeter", "Python"],
        "keywords": ["测试用例", "缺陷管理", "质量保障", "持续集成"],
    },
    "运维": {
        "skills": ["Linux", "Docker", "Kubernetes", "Jenkins", "Shell", "监控告警"],
        "keywords": ["部署运维", "故障排查", "自动化", "高可用"],
    },
}

# ============ 技能知识库 ============

SKILL_DB: dict[str, dict[str, Any]] = {
    # 编程语言
    "Java": {"category": "编程语言", "level": "backend"},
    "Python": {"category": "编程语言", "level": "fullstack"},
    "Go": {"category": "编程语言", "level": "backend"},
    "JavaScript": {"category": "编程语言", "level": "frontend"},
    "TypeScript": {"category": "编程语言", "level": "frontend"},
    "C++": {"category": "编程语言", "level": "system"},
    "Rust": {"category": "编程语言", "level": "system"},
    # 框架
    "Vue": {"category": "前端框架", "level": "frontend"},
    "React": {"category": "前端框架", "level": "frontend"},
    "Spring Boot": {"category": "后端框架", "level": "backend"},
    "Django": {"category": "后端框架", "level": "backend"},
    "FastAPI": {"category": "后端框架", "level": "backend"},
    "Express": {"category": "后端框架", "level": "backend"},
    # 数据库
    "MySQL": {"category": "数据库", "level": "backend"},
    "PostgreSQL": {"category": "数据库", "level": "backend"},
    "MongoDB": {"category": "数据库", "level": "backend"},
    "Redis": {"category": "数据库", "level": "backend"},
    # 中间件
    "Kafka": {"category": "消息队列", "level": "backend"},
    "RabbitMQ": {"category": "消息队列", "level": "backend"},
    "Elasticsearch": {"category": "搜索引擎", "level": "backend"},
    # 云原生
    "Docker": {"category": "容器化", "level": "devops"},
    "Kubernetes": {"category": "容器编排", "level": "devops"},
    "Jenkins": {"category": "CI/CD", "level": "devops"},
    "Nginx": {"category": "Web服务器", "level": "devops"},
    # AI
    "PyTorch": {"category": "深度学习", "level": "ai"},
    "TensorFlow": {"category": "深度学习", "level": "ai"},
    "机器学习": {"category": "AI", "level": "ai"},
    "深度学习": {"category": "AI", "level": "ai"},
    "NLP": {"category": "AI", "level": "ai"},
    "计算机视觉": {"category": "AI", "level": "ai"},
}

# ============ 项目模板库 ============

PROJECT_TEMPLATES: dict[str, list[dict[str, Any]]] = {
    "支付系统": [
        {
            "name": "支付核心系统",
            "description": "负责支付核心模块的设计与开发，包括订单创建、支付渠道对接、对账结算等核心流程。",
            "achievements": [
                "支撑日均交易量 {volume} 笔，交易金额 {amount} 万元",
                "支付成功率达到 {rate}%，系统可用性 {uptime}%",
                "优化支付链路，将支付响应时间从 {old_ms}ms 降低至 {new_ms}ms",
            ],
        },
    ],
    "用户系统": [
        {
            "name": "用户增长系统",
            "description": "负责用户注册、登录、用户画像、推荐等核心功能开发。",
            "achievements": [
                "支撑 {users} 万用户的日常访问，日活 {dau} 万",
                "优化登录流程，登录成功率从 {old_rate}% 提升至 {new_rate}%",
                "设计用户画像系统，推荐点击率提升 {ctr}%",
            ],
        },
    ],
    "电商系统": [
        {
            "name": "商品与订单系统",
            "description": "负责商品管理、购物车、订单创建、库存扣减等核心电商链路开发。",
            "achievements": [
                "支撑大促期间 {qps} QPS 的峰值流量",
                "优化订单创建流程，将下单耗时从 {old_s}s 降低至 {new_s}s",
                "设计库存预扣方案，超卖率降低至 {rate}%",
            ],
        },
    ],
    "数据平台": [
        {
            "name": "数据采集与分析平台",
            "description": "负责数据采集、清洗、存储、可视化等全链路数据平台建设。",
            "achievements": [
                "日处理数据量达到 {tb}TB，数据延迟控制在 {delay} 分钟内",
                "搭建数据看板，覆盖 {metrics} 个核心业务指标",
                "优化查询性能，报表生成时间从 {old_min}min 降低至 {new_min}s",
            ],
        },
    ],
    "管理系统": [
        {
            "name": "后台管理系统",
            "description": "负责企业后台管理系统的设计与开发，包括权限管理、数据看板、操作日志等功能。",
            "achievements": [
                "覆盖 {modules} 个业务模块，{users} 人日常使用",
                "实现权限精细化管理，支持 {roles} 种角色配置",
                "优化数据加载速度，页面首屏加载时间降低 {percent}%",
            ],
        },
    ],
}

# ============ 成就量化模板 ============

ACHIEVEMENT_TEMPLATES: dict[str, list[str]] = {
    "性能优化": [
        "优化{target}，将{metric}从{old}降低至{new}，提升{percent}%",
        "重构{module}模块，{metric}提升{percent}%，节省服务器资源{resource}%",
        "引入{tech}方案，{metric}从{old}优化至{new}",
    ],
    "用户增长": [
        "负责{feature}功能上线，用户{metric}提升{percent}%",
        "优化{path}流程，{metric}从{old}提升至{new}",
        "设计{strategy}策略，{metric}增长{percent}%",
    ],
    "系统稳定性": [
        "保障系统{uptime}%可用性，支撑{scale}并发访问",
        "建立{monitor}监控体系，故障发现时间缩短至{time}分钟",
        "主导系统容灾改造，RTO从{old}降低至{new}",
    ],
    "成本优化": [
        "优化{resource}使用，年度成本降低{amount}万元",
        "重构{module}架构，服务器资源占用降低{percent}%",
        "引入{tech}技术方案，{metric}降低{percent}%",
    ],
}

# ============ 行业术语库 ============

INDUSTRY_TERMS: dict[str, list[str]] = {
    "互联网": ["敏捷开发", "Scrum", "CI/CD", "微服务", "DevOps", "A/B测试", "用户增长", "DAU", "MAU", "ARPU"],
    "金融": ["风控", "合规", "清算", "结算", "对账", "反洗钱", "KYC", "量化", "资管"],
    "电商": ["GMV", "转化率", "复购率", "客单价", "SKU", "SPU", "库存周转", "履约"],
    "AI": ["模型训练", "推理部署", "特征工程", "数据标注", "Fine-tuning", "Prompt Engineering", "RAG"],
}

# ============ 动词库（用于成就描述） ============

ACTION_VERBS: dict[str, list[str]] = {
    "技术": ["设计", "开发", "重构", "优化", "搭建", "主导", "负责", "实现", "攻克", "封装"],
    "管理": ["统筹", "协调", "推动", "规划", "制定", "组织", "带领", "分配", "监督", "评估"],
    "业务": ["分析", "挖掘", "洞察", "提升", "增长", "转化", "留存", "活跃", "变现", "降本"],
}
