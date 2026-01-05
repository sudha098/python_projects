import time
import random
from typing import Callable, Any

def retry(
    func : Callable[[], Any],
    retries : int = 3,
    base_delay : int = 1,
    max_delay : int = 10
) -> Any:

    """
    Retry a function with exponential delay and jitter.
    """
    last_exception = None

    for attempt in range(retries):
        try:
            return func()
        except Exception as exc:
            last_exception = exc
            if attempt == retries - 1:
                break
            delay = min(base_delay * (2 ** attempt), max_delay)
            delay += random.uniform(0, 0.5)
            time.sleep(delay)
    raise RuntimeError("Retries exhausted") from last_exception

counter = {"count": 0}

def flaky_function():
    counter["count"] += 1
    print(f"Attempt #{counter['count']}")

    if counter["count"] < 3:
        raise Exception("Temporary failure")

    return "SUCCESS"

try:
    result = retry(flaky_function, retries=5)
    print("Final result:", result)
except RuntimeError as e:
    print("Retry failed:", e)

print("Total attempts:", counter["count"])

