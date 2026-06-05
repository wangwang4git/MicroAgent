#!/usr/bin/env python3

import os
import subprocess
from dataclasses import dataclass
import anthropic

client = anthropic.Anthropic(base_url='http://localhost:11434', api_key='ollama')
MODEL = 'qwen3:latest'

SYSTEM = (
    f"You are a coding agent at {os.getcwd()}."
    "Use bash to inspect and change the workspace. Act first, then report clearly."
)

TOOLS = [{
    "name": "bash",
    "description": "Run a shell command in the current workspace.",
    "input_schema": {
        "type": "object",
        "properties": {"command": {"type": "string"}},
        "required": ["command"],
    },
}]

@dataclass
class LoopState:
    messages: list
    turn_count: int = 1
    transition_reason: str | None = None

def run_bash(command: str) -> str:
    dangerous = ["rm -rf /", "sudo", "shutdown", "reboot", "> /dev/"]
    if any(item in command for item in dangerous):
        return "Error: Dangerous command blocked"

    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=os.getcwd(),
            capture_output=True,
            text=True,
            timeout=120,
        )
    except subprocess.TimeoutExpired:
        return "Error: Timeout (120s)"
    except (FileNotFoundError, OSError) as e:
        return f"Error: {e}"

    output = (result.stdout + result.stderr).strip()
    return output[:50000] if output else "(no output)"

def extract_text(content) -> str:
    if not isinstance(content, list):
        return ""

    texts = []
    for block in content:
        text = getattr(block, "text", None)
        if text:
            texts.append(text)

    return "\n".join(texts).strip()

def execute_tool_calls(response_content) -> list[dict]:
    results = []
    for block in response_content:
        if block.type != "tool_use":
            continue

        command = block.input["command"]
        print(f"{command}")

        output = run_bash(command)
        print(output[:200])

        results.append({
            "type": "tool_result",
            "tool_use_id": block.id,
            "content": output,
        })
    return results

def run_one_turn(state: LoopState) -> bool:
    response = client.messages.create(
        model=MODEL,
        system=SYSTEM,
        messages=state.messages,
        tools=TOOLS,
        max_tokens=8000,
    )
    state.messages.append({"role": "assistant", "content": response.content})
    # print(response.content)

    if response.stop_reason != "tool_use":
        state.transition_reason = None
        return False

    results = execute_tool_calls(response.content)
    if not results:
        state.transition_reason = None
        return False

    state.messages.append({"role": "user", "content": results})
    state.turn_count += 1
    state.transition_reason = "tool_result"
    return True

def agent_loop(state: LoopState) -> None:
    while run_one_turn(state):
        pass

if __name__ == "__main__":
    history = []
    while True:
        try:
            query = input("s01 >> ")
        except (EOFError, KeyboardInterrupt):
            break

        if query.strip().lower() in ("q", "quit", "exit", ""):
            break

        history.append({"role": "user", "content": query})
        state = LoopState(messages=history)
        agent_loop(state)

        final_text = extract_text(history[-1]["content"])
        if final_text:
            print(final_text)

        print()
