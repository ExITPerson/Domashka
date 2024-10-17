from operator import itemgetter

from black import datetime

from src.widget import get_date


def filter_by_state(user_list: list[dict], state: str = "EXECUTED") -> list[dict] or str:
    """
    Функция принимает список словарей, создает новый словрь,
    фильтруя список по значению ключа "state".
    """
    if any(user_list):
        return [user for user in user_list if user["state"] == state]
    return "Нет данных о юзерах"


def sort_by_date(user_list: list[dict], sort_bool: bool = True) -> list[dict] or str:
    """Фуркция принимает список и сортирует его по значению ключа "date"."""
    try:
        for user in user_list:
            if get_date(user['date']) == "Не корректный формат даты":
                user['date'] = "2001-01-01T01:01:01.512364"
        if any(user_list):
            return sorted(user_list, key=itemgetter("date", "id"), reverse=True)
        return "Нет данных о юзерах"
    except KeyError:
        return "Нет данных о юзерах"
