"""Configuration management — loads settings from environment variables."""

from __future__ import annotations

from typing import Any, Optional


class Settings:
    """Application settings loaded from environment variables."""

    def __init__(self) -> None:
        ...

    @property
    def llm_provider(self) -> str:
        ...

    @property
    def llm_model(self) -> str:
        ...

    @property
    def llm_api_key(self) -> Optional[str]:
        ...

    @property
    def llm_base_url(self) -> Optional[str]:
        ...

    @property
    def log_level(self) -> str:
        ...

    def get(self, key: str, default: Any = None) -> Any:
        """Get a setting by key, with an optional default."""
        ...


# Singleton instance
settings = Settings()
