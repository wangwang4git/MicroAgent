"""Agent — the central orchestrator that drives LLM interactions with tools and memory."""

from __future__ import annotations

from typing import Any, Optional, Sequence

from pydantic import BaseModel, Field


class AgentConfig(BaseModel):
    """Configuration for an Agent instance."""

    name: str = Field(default="MicroAgent")
    system_prompt: str = Field(default="You are a helpful AI assistant.")
    max_tool_calls: int = Field(default=10, ge=1)
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(default=4096, ge=1)


class Agent:
    """A lightweight AI agent that orchestrates LLM calls with tools and memory."""

    def __init__(
        self,
        llm: Any,
        *,
        system_prompt: Optional[str] = None,
        tools: Optional[Sequence[Any]] = None,
        memory: Optional[Any] = None,
        config: Optional[AgentConfig] = None,
    ) -> None:
        ...

    @property
    def name(self) -> str:
        ...

    def register_tool(self, tool: Any) -> None:
        """Register a tool that the agent can invoke."""
        ...

    def unregister_tool(self, name: str) -> None:
        """Remove a previously registered tool."""
        ...

    async def run(self, user_input: str, **kwargs: Any) -> str:
        """Execute the agent on a user query, returning the final text response."""
        ...

    async def chat(self) -> None:
        """Start an interactive chat session (for REPL / CLI use)."""
        ...

    def reset(self) -> None:
        """Clear conversation history (preserves system prompt)."""
        ...
