from functools import wraps
from typing import Any, Callable


def log(filename: str = None) -> Any:
    """ Декоратор, который выводит результат работы функции на консоль, либо создает файл с результатами"""

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            if filename is not None:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(f"Начало работы функции: {func.__name__}\n")
                    try:
                        result = func(*args, **kwargs)
                        f.write(f"Конец работы функции: {func.__name__}\nРезультат работы: {result}")
                    except Exception as e:
                        f.write(
                            f"""Конец работы функции: {func.__name__}\nОшибка: {e}\nВходные параметры: {args or kwargs}
Исключение: {type(e).__name__}"""
                        )
            else:
                print(f"Начало работы функции: {func.__name__}")
                try:
                    result = func(*args, **kwargs)
                    return f"""Конец работы функции: {func.__name__}\nРезультат работы: {result}"""
                except Exception as e:
                    return f"""Конец работы функции: {func.__name__}\nОшибка: {e}\nВходные параметры: {args or kwargs}
Исключение: {type(e).__name__}"""

        return inner

    return wrapper
