from __future__ import annotations

from typing import Protocol

from langchain_anthropic import ChatAnthropic
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_openai import ChatOpenAI


class ChatModelConfig(Protocol):
    provider: str
    api_key: str
    base_url: str
    model: str
    temperature: float
    timeout: int
    max_tokens: int | None


def create_chat_model(config: ChatModelConfig, timeout: int | None = None) -> BaseChatModel:
    """Build the correct LangChain client for an OpenAI- or Anthropic-compatible endpoint."""
    request_timeout = max(int(config.timeout or 0), int(timeout or 0)) if timeout else int(config.timeout or 60)
    max_tokens = int(config.max_tokens or 8192)
    provider = (config.provider or "openai-compatible").strip().lower()

    if provider in {"anthropic", "anthropic-compatible"}:
        return ChatAnthropic(
            api_key=config.api_key,
            base_url=config.base_url,
            model_name=config.model,
            temperature=float(config.temperature),
            timeout=request_timeout,
            max_tokens_to_sample=max_tokens,
        )

    return ChatOpenAI(
        api_key=config.api_key,
        base_url=config.base_url,
        model=config.model,
        temperature=float(config.temperature),
        timeout=request_timeout,
        max_tokens=max_tokens,
    )
