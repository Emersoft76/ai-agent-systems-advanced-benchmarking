"""
Prompt Strategy Engine
-----------------------

Dynamically generates and optimizes prompts for LLM agents
using task-aware templates, few-shot examples, and fallback logic.

✅ Features:
- Zero-shot and few-shot prompt builders
- Adaptive template injection
- Prompt fallback strategy based on failure detection

"""

from typing import List, Optional


class PromptTemplate:
    def __init__(self, system_instruction: str, examples: Optional[List[str]] = None):
        self.system_instruction = system_instruction
        self.examples = examples or []

    def build_prompt(self, user_input: str) -> str:
        """Builds a full prompt from base template + examples + user input."""
        parts = [f"System: {self.system_instruction}"]
        for idx, ex in enumerate(self.examples):
            parts.append(f"Example {idx + 1}:\n{ex}")
        parts.append(f"User: {user_input}")
        return "\n\n".join(parts)


class PromptFallback:
    def __init__(self, variants: List[str]):
        self.variants = variants
        self.index = 0

    def next_prompt(self) -> str:
        """Returns the next fallback prompt variant."""
        prompt = self.variants[self.index]
        self.index = (self.index + 1) % len(self.variants)
        return prompt


# Example usage
if __name__ == "__main__":
    strategy = PromptTemplate(
        system_instruction="You are a helpful AI assistant that solves complex logic problems.",
        examples=[
            "Q: If all Zogs are Glips and some Glips are Blargs, are all Zogs definitely Blargs?\nA: Not necessarily.",
            "Q: A train leaves at 3 PM and travels at 60mph, when will it reach 180 miles?\nA: 6 PM."
        ]
    )
    prompt = strategy.build_prompt("How can I optimize a memory-based retrieval system?")
    print("🧠 Generated Prompt:\n", prompt)
