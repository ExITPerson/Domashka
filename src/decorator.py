from typing import Any
from functools import wraps

def log(filename: str = None) -> Any :
    def wrapper(func):
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            if filename is not None:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(f"Начало работы функции: {func.__name__}\n")
                    try:
                        result = func(*args, **kwargs)
                        f.write(f"""
Конец работы функции: {func.__name__} 
Результат работы: {result}""")
                    except Exception as e:
                        return f.write(f"""
Конец работы функции: {func.__name__} 
Ошибка: {e}
Входные параметры: {args or kwargs}
Исключение: {type(e).__name__}
""")
            else:
                print(f"Начало работы функции\n {func.__name__}\n")
                try:
                    result = func(*args, **kwargs)
                    return f"""
Конец работы функции: {func.__name__} 
Результат работы: {result}
"""
                except Exception as e:
                    return f"""
Конец работы функции: {func.__name__} 
Ошибка: {e}
Входные параметры: {args or kwargs}
Исключение: {type(e).__name__}
"""
        return inner
    return wrapper

