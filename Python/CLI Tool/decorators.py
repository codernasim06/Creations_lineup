import functools
import time
import sys
from typing import Any, Callable

def async_timed():
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time.perf_counter()
            try:
                return await func(*args, **kwargs)
            finally:
                end_time = time.perf_counter()
                elapsed = end_time - start_time
                print(f"[Telemetry] Functional module `{func.__name__}` resolved in {elapsed:.3f}s", file=sys.stderr)
        return wrapper
    return decorator

def handle_api_errors():
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return await func(*args, **kwargs)
            except Exception as exc:
                print(f"\n❌ Pipeline Execution Failure in `{func.__name__}` : {exc}", file = sys.stderr)
                print("💡 Tip: Verify username targets, target tokens, and net routing states.", file = sys.stderr)
                sys.exit(1)
        return wrapper
    return decorator