"""
Agent Self-Reflection Example
-----------------------------

🧠 Purpose:
This script demonstrates an agent that can evaluate its own responses
and revise them using a self-reflection chain.

📦 Requirements:
- openai
- langchain >= 0.1.0
- python-dotenv

"""

import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import SelfCritiqueChain
from langchain.agents import Tool, initialize_agent
from langchain.tools import DuckDuckGoSearchRun

# 🔐 Load your API key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 🧠 Base LLM
llm = ChatOpenAI(model="gpt-4", temperature=0.7)

# 🔎 Add a simple external tool (search)
search = DuckDuckGoSearchRun()
tools = [Tool(name="DuckDuckGoSearch", func=search.run, description="Search tool")]

# 🤖 Create base agent
agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

# 🔁 Self-reflection Chain
critique_chain = SelfCritiqueChain.from_llm(llm)

# 🧪 Prompt & test case
query = "What are the health benefits of green tea?"

print("\n🔍 Initial Agent Response:")
response = agent.run(query)
print(response)

print("\n🧠 Agent Self-Reflection:")
reflection = critique_chain.run(input=response)
print(reflection)

# ✅ Outcome:
# The agent will critique and revise its own output for higher factual consistency.
