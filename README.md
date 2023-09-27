# Drawing_nested_triangles_itog
[![Build, Test](https://github.com/Zhukkovaa/Drawing_nested_triangles/actions/workflows/python-app.yml/badge.svg)](https://github.com/Zhukkovaa/Drawing_nested_triangles/actions/workflows/python-app.yml)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Zhukkovaa/Drawing_nested_triangles_itog?color=coral)
[![License: MIT ](https://img.shields.io/badge/License-MIT-violet.svg)](https://opensource.org/licenses/MIT)
# Лабораторная работа по дисциплине "Компьютерная графика" №1. 
### Демонстрация выполнения работы программы с шагом уменьшения длины сторон на h = 80
![Анимация](https://github.com/Zhukkovaa/Drawing_nested_triangles_itog/blob/main/giffffochka/bolshe.gif)
# Описание задачи
Вариант 9. Необходимо реализовать программу, которая выводила бы на экран вложенные равносторонние треугольники. При этом каждый очередной треугольник должен выводиться при нажатии клавиши Enter, а при
нажатии клавиши D убирался бы последний построенный. Выход по ESC. Треугольники должны выводиться с заданным шагом уменьшения размера его сторон h.
## Программа реализована на языке:

| Язык | Интерпретатор/Версия | Среда разработки | 
| ------ | ------ | ------ |
| Python | Python / w64 3.11 | PyCharm 2022 3.2 |

## Используемые библиотеки:
* tkinter - для создания графического пользовательского интерфейса (GUI)
* unittest - для написания и выполнения тестов

## Описание возможностей:
- Ввод параметра h для уменьшения длин сторон равностороннего треугольника;
- Валидация полей (проверка на ввод отрицательных чисел, букв и других недопустимых символов);
- Построение каждого последующего вложенного треугольника при нажатии клавиши Enter;
- Удаление последнего построенного треугольника при нажатии клавиши D;
- Выход из программы при нажатии клавиши Esc.

## Установка и запуск:
1. ```git clone https://github.com/Zhukkovaa/Drawing_nested_triangles.git```
2. ```cd <your_project_folder>```
3. ```python3.11 main.py```

