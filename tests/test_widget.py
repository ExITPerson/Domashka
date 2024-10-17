from typing import Any

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "name_and_number, expected",
    [
        ("Master Card 7000792289606361", "Master Card 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(name_and_number: Any, expected: Any) -> Any:
    assert mask_account_card(name_and_number) == expected


def test_mask_account_card_with_negative_number(negative_card_number: Any) -> Any:
    for i in negative_card_number:
        with pytest.raises(ValueError):
            mask_account_card(i)


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2022-10-12T02:26:18.671407", "12.10.2022"),
        ("11.03.2024", "Не корректный формат даты"),
        ("", "Не корректный формат даты"),
    ],
)
def test_get_date(date: str, expected: str) -> None:
    assert get_date(date) == expected
