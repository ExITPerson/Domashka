![b3a5a00f-6e6b-488f-9ac1-5623c31cb0d1.jpg](design_tools%2Fb3a5a00f-6e6b-488f-9ac1-5623c31cb0d1.jpg)

# <p align="center"> Домашка </p>


## <p align="center">Описание</p>

**<p align="center">Домашка - это проект для выполнения "Домашек", учась в SkyPro на разработчика Python.</p>**

---

## <p align="center">Функции программы</p>


- **Сортировка по дате платежа**
- **Фильтрация по статусу платежа**
- **Фильтрация по коду валюты** 
- **Вывод назначения всех платежей** 
- **Генерация номера карт** 
- **Максировка номера карт и счетов** 


----

## <p align="center">Установка</p>

1. **Клонируйте репозиторий:**
````
git clone https://github.com/ExITPerson/Domashka.git
````

2. **Установите зависимости:**
````
pip install -r requirements.txt
````
---

## <p align="center">Информация о тестировании проекта</p>

- **Запустите тестирование**
````
pytest --cov src --cov-report term-missing
````

- **Увидите информацию о тестах папки scr в терминале**

````
======================================= test session starts ===========================================================
platform win32 -- Python 3.12.6, pytest-8.3.3, pluggy-1.5.0
rootdir:
configfile: pyproject.toml
plugins: cov-5.0.0
collected 24 items                                                                                                                                                                 

tests\test_generator.py ........                                                 [ 33%]
tests\test_masks.py ......                                                       [ 58%] 
tests\test_processing.py ...                                                     [ 70%]
tests\test_widget.py .......                                                     [100%]


---------- coverage: platform win32, python 3.12.6-final-0 -----------
Name                Stmts   Miss  Cover   Missing
-------------------------------------------------
src\__init__.py         0      0   100%
src\masks.py           12      0   100%
src\processing.py      17      0   100%
src\widget.py          23      0   100%
src\generators.py      22      0   100%
-------------------------------------------------
TOTAL                  74      0   100%


=============================== 24 passed in 1.15s ==================================================================== 
````