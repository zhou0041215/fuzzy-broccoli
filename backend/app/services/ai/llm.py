from langchain_core.language_models.chat_models import BaseChatModel

from app.services.ai_config_service import get_active_ai_config
from app.services.ai.chat_model_factory import create_chat_model


def get_llm(timeout: int | None = None) -> BaseChatModel:
    config = get_active_ai_config()
    return create_chat_model(config, timeout)
