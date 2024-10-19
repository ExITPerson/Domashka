from datetime import datetime


def mask_account_card(input_information: str) -> str:
    """Функция маскирует данные карты, либо счета"""
    try:
        numbers = "".join([str(num) for num in input_information if num.isdigit()])
        string = " ".join([i for i in input_information.split(" ") if i.isalpha()])
        if len(numbers) and len(string):
            if len(numbers) == 20:
                from src.masks import get_mask_account

                return f"{string} {get_mask_account(numbers)}"
            elif len(numbers) == 16:
                from src.masks import get_mask_card_number

                return f"{string} {get_mask_card_number(numbers)}"
            else:
                raise ValueError("Введены некорректные данные, попробуйте снова.")
        else:
            raise ValueError("Введены некорректные данные, попробуйте снова.")
    except:
        raise ValueError("Введены некорректные данные, попробуйте снова.")


def get_date(date_time: str) -> str:
    """Функция преобразовывает принимаемую дату в формат "ДД.ММ.ГГГГ" """
    try:
        date = datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%S.%f")
        new_date = date.strftime("%d.%m.%Y")
        return new_date
    except ValueError:
        return "Не корректный формат даты"