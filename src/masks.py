from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция выводит номер карты с замаскированными элементами"""
    if len(str(card_number)) == 16:
        mask_card = f"{str(card_number)[0:6]}******{str(card_number)[-4:]}"
        return f"{mask_card[0:4]} {mask_card[4:8]} {mask_card[8:12]} {mask_card[-4:]}"
    else:
        return "Номер карты введен не корректно, попробуйте еще."


def get_mask_account(card_number: Union[str, int]) -> str:
    """Функция выводит последние 6 элементов номера карты с маскировкой первых двух"""
    if len(str(card_number)) == 20:
        return f"**{str(card_number)[-4:]}"
    else:
        return "Номер карты введен не корректно, попробуйте еще."
