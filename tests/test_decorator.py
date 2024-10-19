import os

from src.decorator import log


def test_log(capsys) -> None:
    """Тестируем вывод в консоль"""

    @log()
    def positive_number(numb: int) -> str:
        if numb > 0:
            return "Число положительное"
        else:
            raise ValueError("Число должно быть положительным")

    result = positive_number(2)
    captured = capsys.readouterr()
    assert captured.out == "Начало работы функции: positive_number\n"
    assert result == "Конец работы функции: positive_number\nРезультат работы: Число положительное"

    result = positive_number(-1)
    captured = capsys.readouterr()
    assert captured.out == "Начало работы функции: positive_number\n"
    assert (
        result
        == """Конец работы функции: positive_number
Ошибка: Число должно быть положительным
Входные параметры: (-1,)
Исключение: ValueError"""
    )


def test_log_to_create_a_file_positive() -> None:
    @log("log.txt")
    def positive_number_file(numb: int) -> str:
        if numb > 0:
            return "Число положительное"
        else:
            raise ValueError("Число должно быть положительным")

    positive_number_file(2)
    assert os.path.exists("log.txt")

    with open("log.txt", "r", encoding="utf-8") as f:
        log_content = f.read()

        assert "Начало работы функции: positive_number_file" in log_content
        assert "Конец работы функции: positive_number_file" in log_content
        assert "Результат работы: Число положительное" in log_content


def test_log_to_create_a_file_negative() -> None:
    @log("log_negative.txt")
    def negative_number_file(numb: int) -> str:
        if numb > 0:
            return "Число положительное"
        else:
            raise ValueError("Число должно быть положительным")

    negative_number_file(-1)
    assert os.path.exists("log_negative.txt")

    with open("log_negative.txt", "r", encoding="utf-8") as f:
        log_content = f.read()

        assert "Начало работы функции: negative_number_file" in log_content
        assert "Конец работы функции: negative_number_file" in log_content
        assert "Ошибка: Число должно быть положительным" in log_content
        assert "Входные параметры: (-1,)" in log_content
        assert "Исключение: ValueError" in log_content
