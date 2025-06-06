"""
Run Demo Agent Interaction
---------------------------

This script loads a demo LLM agent and performs a sample query
to showcase functionality and validate installation.
"""

from src.core.agent import AIAgent

if __name__ == "__main__":
    agent = AIAgent(name="DemoAgent")
    query = "Summarize the history of the Internet in 3 sentences."
    result = agent.run(query)
    print(f"\n🤖 Agent Response:\n{result}\n")
