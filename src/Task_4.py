def circle_area(r: float) -> float:
    """Функция находит область окружности"""
    pi = 3.14
    return float(pi * r**2)


def format_description(r: float, area: float) -> str:
    """Функция выводит информацию типа str о круге"""
    return "Radius is " + str(r) + "; area is " + str(round(area, 2))


def get_info(r: float) -> None:
    """Функция принимает значение и преобразует его для дальнейших вычеслений"""
    area = circle_area(r)
    description = format_description(r, area)
    print(description)


radius = int(input("Enter circle radius (int): "))
get_info(radius)
