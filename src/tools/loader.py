"""
Tool Loader
------------

Dynamically loads and registers tools into the AI agent environment.

✅ Responsibilities:
- Tool discovery and validation
- Custom tool registration
- Interface with agent planner

"""

from typing import List, Dict

# Simulated registry of available tools
AVAILABLE_TOOLS = {
    "web_search": lambda query: f"🔍 Searching the web for: {query}",
    "calculator": lambda expression: f"🧮 Result: {eval(expression)}",
    "file_reader": lambda path: f"📄 Reading file at: {path}"
}


def load_tools(tool_names: List[str]) -> Dict[str, callable]:
    loaded = {}
    for tool in tool_names:
        if tool in AVAILABLE_TOOLS:
            loaded[tool] = AVAILABLE_TOOLS[tool]
            print(f"✅ Loaded tool: {tool}")
        else:
            print(f"⚠️ Tool '{tool}' not found in registry.")
    return loaded


def register_tool(name: str, function: callable):
    if name in AVAILABLE_TOOLS:
        print(f"🔁 Overwriting existing tool: {name}")
    AVAILABLE_TOOLS[name] = function
    print(f"🛠️ Registered new tool: {name}")
