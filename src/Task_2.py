def identification_of_a_palindrome(lst: list[int]) -> list[int]:
    """Функция, которая находит палидром из принимаемого списка"""
    return [int(element) for element in lst if str(element) == str(element)[::-1]]
