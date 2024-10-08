def generation_uni_list(lst_1: list[int], lst_2: list[int]) -> list[int]:
    """Функция, которая находит пересечения двух принимаемых списков"""
    return [num for num in lst_1 if num in lst_2]
