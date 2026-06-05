"""Command-line interface for MicroAgent."""

from __future__ import annotations

import click


@click.group()
def main() -> None:
    """MicroAgent — lightweight AI agent framework CLI."""
    ...


@main.command()
@click.argument("query")
def run(query: str) -> None:
    """Run a single query through the agent."""
    ...


@main.command()
def chat() -> None:
    """Start an interactive chat session."""
    ...


@main.group()
def tools() -> None:
    """Manage agent tools."""
    ...


@tools.command(name="list")
def tools_list() -> None:
    """List available tools."""
    ...
