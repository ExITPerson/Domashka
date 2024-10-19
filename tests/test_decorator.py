#import pytest

from src.decorator import log

@log("log.txt")
def number_true(numb):
    if numb > 0:
        return "Число положительное"
    else:
        raise ValueError("Число должно быть положительным")

n = number_true(2)
print(n)