from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator:
    """Функция, выводящая отсортированные операции по валюте"""
    if any(transactions):
        filter_transactions = [
            x
            for x in transactions
            if x.get("operationAmount") and x["operationAmount"]["currency"]["code"] == currency
        ]
        index = len(filter_transactions)
        if any(filter_transactions):
            for transaction in filter_transactions:
                yield transaction
                index -= 1
        else:
            yield "Транзакций не обнаружено"
    else:
        yield "Транзакций не обнаружено"


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """Функция, выводящая типы транзакций"""
    if any(transactions):
        for transaction in transactions:
            if transaction["description"]:
                yield transaction["description"]
    else:
        yield "Транзакций не обнаружено"


def card_number_generator(start: int, stop: int) -> Generator:
    """Функция генерирующая номера карт"""
    for num in range(start, stop + 1):
        card_number = f'{"0" * (16 - len(str(num))) + str(num)}'
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number
