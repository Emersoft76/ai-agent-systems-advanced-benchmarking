"""
Test GAIA Benchmark Scoring
----------------------------

This test validates whether the current agent setup reaches a minimum threshold
benchmark score using a mock or reduced GAIA-style task set.

Run with: pytest tests/test_benchmark_score.py
"""

import pytest
from src.core.agent import AIAgent
from src.utils.timer import timed

@timed
def evaluate_benchmark(agent: AIAgent) -> float:
    mock_tasks = [
        {"question": "What is the capital of Germany?", "answer": "Berlin"},
        {"question": "Translate 'gato' from Spanish to English.", "answer": "cat"},
    ]
    score = 0
    for task in mock_tasks:
        response = agent.run(task["question"])
        if task["answer"].lower() in response.lower():
            score += 1
    return score / len(mock_tasks)

def test_agent_benchmark():
    agent = AIAgent(name="BenchmarkBot")
    result = evaluate_benchmark(agent)
    assert result >= 0.5, f"Benchmark too low: {result:.2f}"
