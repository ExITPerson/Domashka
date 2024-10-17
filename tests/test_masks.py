import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number, expected",
    [
        ("77663800506351", "Номер карты не соответствует формату (16 цифр)"),
        ("", "Номер карты не соответствует формату (16 цифр)"),
        (7000896063005100, "7000 89** **** 5100"),
    ],
)
def test_get_mask_card_number(number: str, expected: str) -> None:
    assert get_mask_card_number(number) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        ("77663800506351", "Номер карты не соответствует формату (16 цифр)"),
        ("", "Номер карты не соответствует формату (16 цифр)"),
        (70008960630051003798, "**3798"),
    ],
)
def test_get_mask_account(number: str, expected: str) -> None:
    assert get_mask_account(number) == expected
