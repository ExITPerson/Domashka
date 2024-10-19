from typing import Any

def log(filename: str=None) -> Any:
    def wrapper(func):
        def inner(*args: Any, **kwargs: Any) -> Any:
            result = func(*args, **kwargs)
        return inner
    return wrapper