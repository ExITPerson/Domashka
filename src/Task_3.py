def unifying_lists(lst_1: list[int], lst_2: list[int]) -> list[int]:
    """Функция возвращает список из чисел, которые не пересекаются в передаваемых списках."""
    return list(set(lst_1) - set(lst_2)) + list(set(lst_2) - set(lst_1))
