"""
Execution Timer
----------------

Utility for measuring runtime of code blocks or function calls.

✅ Features:
- Context manager for scoped timing
- Decorator for function execution timing
- Useful in benchmarking, profiling, or GAIA evaluations

"""

import time
from functools import wraps

class Timer:
    def __init__(self, name: str = "⏱️ Elapsed"):
        self.name = name

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        print(f"{self.name}: {self.end - self.start:.4f} seconds")

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"⏲️ {func.__name__} took {elapsed:.4f} seconds")
        return result
    return wrapper


# Example usage
if __name__ == "__main__":
    @timed
    def simulated_task():
        time.sleep(1.25)
        return "✅ Done"

    with Timer("🔍 Prompt generation"):
        time.sleep(0.7)

    simulated_task()
