# MicroAgent

A lightweight, extensible AI agent framework built with Python.

## Features

- **Modular Architecture** — Pluggable LLM providers, tools, and memory backends
- **Type-Safe** — Full Pydantic models for reliable data handling
- **Async First** — Built on asyncio for high-concurrency agent workflows
- **CLI Interface** — Rich command-line tool for quick experimentation
- **Extensible** — Simple interfaces for custom tools and providers

## Installation

```bash
git clone <repo-url>
cd MicroAgent
pip install -e .

# With dev dependencies
pip install -e ".[dev]"
```

## Quick Start

```python
# TODO: add quick start example
```

## Project Structure

```
MicroAgent/
├── src/microagent/       # Main package
│   ├── core/             # Core abstractions (Agent, Tool, Memory)
│   ├── llm/              # LLM provider integrations
│   ├── utils/            # Config, logging, helpers
│   └── cli.py            # CLI entry point
├── tests/                # Test suite
├── examples/             # Usage examples
└── pyproject.toml        # Project metadata & dependencies
```

## Configuration

Set environment variables or create a `.env` file:

```bash
MICROAGENT_LLM_PROVIDER=openai
MICROAGENT_LLM_MODEL=gpt-4o-mini
MICROAGENT_LLM_API_KEY=sk-...
```

## License

MIT
