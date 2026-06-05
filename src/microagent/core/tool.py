"""Tool abstraction — defines how agents interact with external functions."""

from __future__ import annotations

from typing import Any, Callable, Optional

from pydantic import BaseModel, Field


class Tool(BaseModel):
    """Represents a callable tool that an agent can use."""

    name: str = Field(...)
    description: str = Field(...)
    parameters: dict[str, Any] = Field(default_factory=dict)
    func: Optional[Callable[..., Any]] = Field(default=None, exclude=True)

    model_config = {"arbitrary_types_allowed": True}

    async def execute(self, **kwargs: Any) -> Any:
        """Execute the tool function with the given keyword arguments."""
        ...

    def to_openai_schema(self) -> dict[str, Any]:
        """Return the OpenAI function-calling schema dict."""
        ...


def tool(
    name: Optional[str] = None,
    description: str = "",
) -> Callable[[Callable[..., Any]], Tool]:
    """Decorator to create a Tool from a regular function.

    Usage::

        @tool(name="calculator", description="Evaluate a math expression")
        def calculator(expression: str) -> float:
            ...
    """
    ...
