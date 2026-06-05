"""Memory — conversation history and context management for agents."""

from __future__ import annotations

from typing import Any, Optional


class Memory:
    """Stores and manages conversation messages.

    Parameters:
        max_messages: Maximum number of messages to retain (excluding system).
                      ``None`` means unlimited.
    """

    def __init__(self, max_messages: Optional[int] = 100) -> None:
        ...

    def add_system_message(self, content: str) -> None:
        """Set or overwrite the system message."""
        ...

    def add_user_message(self, content: str) -> None:
        """Append a user message."""
        ...

    def add_assistant_message(
        self,
        content: str,
        tool_calls: Optional[list[dict[str, Any]]] = None,
    ) -> None:
        """Append an assistant message, optionally with tool calls."""
        ...

    def add_tool_results(self, results: list[dict[str, str]]) -> None:
        """Append tool-result messages."""
        ...

    def get_messages(self, include_system: bool = True) -> list[dict[str, Any]]:
        """Return all stored messages as a list (for LLM API calls)."""
        ...

    def get_last_message(self) -> Optional[dict[str, Any]]:
        """Return the most recent message or ``None``."""
        ...

    def clear(self) -> None:
        """Clear all messages (preserves system message)."""
        ...

    def __len__(self) -> int:
        ...
