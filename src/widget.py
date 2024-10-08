import datetime

from masks import get_mask_account
from masks import get_mask_card_number


def mask_account_card(input_information: str) -> str:
    numbers = ''.join([str(num) for num in input_information if num.isdigit()])
    if len(numbers) == 20:
        return get_mask_account(numbers)
    elif len(numbers) == 16:
        return get_mask_card_number(numbers)


def get_date(data_time: str) -> str:
    date = data_time[0:10]
    return f'{date[-2:]}:{date[5:7]}:{date[0:4]}'
