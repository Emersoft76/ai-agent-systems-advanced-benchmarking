"""
Async Pipeline Demo
--------------------

⚙️ Purpose:
Illustrates how to run LLM-based subtasks asynchronously in a pipeline-style architecture.

📦 Requirements:
- langchain >= 0.1.0
- openai
- asyncio
- python-dotenv

"""

import os
import asyncio
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

# 🔐 Load API keys
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 🌐 Base LLM
llm = ChatOpenAI(model="gpt-4", temperature=0.3)

# 🧩 Simulate subtasks
async def extract_keywords(text):
    print("🔍 Extracting keywords...")
    result = await llm.apredict(f"Extract keywords from: {text}")
    return result

async def summarize_text(text):
    print("📝 Summarizing text...")
    result = await llm.apredict(f"Summarize this text: {text}")
    return result

async def classify_topic(text):
    print("🏷️ Classifying topic...")
    result = await llm.apredict(f"Classify topic of this text: {text}")
    return result

# 🎯 Master async pipeline
async def main_pipeline():
    sample_text = (
        "Large language models like GPT-4 are revolutionizing the AI industry by enabling advanced reasoning and generation."
    )

    # Run tasks concurrently
    results = await asyncio.gather(
        extract_keywords(sample_text),
        summarize_text(sample_text),
        classify_topic(sample_text)
    )

    # Display results
    print("\n✅ Pipeline Results:")
    print("Keywords:", results[0])
    print("Summary:", results[1])
    print("Topic:", results[2])

# 🚀 Launch
if __name__ == "__main__":
    asyncio.run(main_pipeline())
