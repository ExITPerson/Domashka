from masks import get_mask_account
from masks import get_mask_card_number


def mask_account_card(input_information):
    numbers = ''.join([str(num) for num in input_information if num.isdigit()])
    if len(numbers) == 20:
        return get_mask_account(numbers)
    elif len(numbers) == 16:
        return get_mask_card_number(numbers)


print(mask_account_card('Card 7365410843013587'))