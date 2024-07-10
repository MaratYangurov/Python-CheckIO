"""
Нашему Робо-Трио необходимо тренироваться для будущих приключений и охоты за сокровищами (золотые контакты нужны всем).
Стефан построил специальную упрощенную модель пирамиды.
И теперь наши роботы будут тренироваться в забегах за золотом на скорость.
Они начинают с вершины пирамиды и собирают золото в каждой комнате, через которую проходят.
В каждой комнате они выбирают влево или вправо и спускаются на следующий уровень.
Чтобы оценивать результаты, Стефану нужно знать, а сколько максимум можно собрать за один забег.

Представьте список списков в котором первый список имеет одно число и следующие на одно число больше чем предыдущий.
Такой список списков будет выглядеть как пирамида.
Тебе нужно написать функцию,
которая поможет Стефану найти максимальную сумму золота на самом выгодном маршруте с вершины пирамиды до ее основания.
Все маршруты прохода по пирамиде из шагов вниз и влево/вправо.

Примечания: Попробуйте думать о шаге вниз-влево,
как о движении в следующий ряд не изменяя индекс в ряду и о шаге вниз/вправо -- с увеличением индекса в ряду на единицу.
Будьте осторожны если вы хотите решать задачу рекурсией, получится медленное решение.
"""

def count_gold(pyramid: list) -> int: # count_gold принимает список списков (пирамиду).
    # replace this for solution
    # Вспомогательная функция для рекурсивного вычисления
    def get_max_gold(row, col): # get_max_gold принимает два параметра: row (текущая строка) и col (текущий столбец).
        # Базовый случай: Если текущая строка (row) — последняя в пирамиде, функция возвращает значение текущей ячейки (pyramid[row][col]).
        if row == len(pyramid) - 1:
            return pyramid[row][col]

        # Рекурсивные вызовы для левой и правой ветвей
        # Функция вычисляет максимальную сумму для левого (left_path) и правого (right_path) путей, начиная с текущей ячейки.
        left_path = get_max_gold(row + 1, col)
        right_path = get_max_gold(row + 1, col + 1)

        # Возвращает текущую ячейку плюс максимальную сумму из двух возможных путей.
        return pyramid[row][col] + max(left_path, right_path)

    # Начинаем с вершины пирамиды
    return get_max_gold(0, 0)

print("Example:")
print(
    count_gold(
        [
            [1],
            [2, 3],
            [3, 3, 1],
            [3, 1, 5, 4],
            [3, 1, 3, 1, 3],
            [2, 2, 2, 2, 2, 2],
            [5, 6, 4, 5, 6, 4, 3],
        ]
    )
)
"""
# These "asserts" are used for self-checking
assert (
    count_gold(
        [
            [1],
            [2, 3],
            [3, 3, 1],
            [3, 1, 5, 4],
            [3, 1, 3, 1, 3],
            [2, 2, 2, 2, 2, 2],
            [5, 6, 4, 5, 6, 4, 3],
        ]
    )
    == 23
)
assert (
    count_gold(
        [
            [1],
            [2, 1],
            [1, 2, 1],
            [1, 2, 1, 1],
            [1, 2, 1, 1, 1],
            [1, 2, 1, 1, 1, 1],
            [1, 2, 1, 1, 1, 1, 9],
        ]
    )
    == 15
)
assert count_gold([[9], [2, 2], [3, 3, 3], [4, 4, 4, 4]]) == 18
assert (
    count_gold(
        [[2], [7, 9], [0, 8, 6], [4, 7, 6, 8], [0, 5, 5, 4, 1], [9, 1, 0, 1, 6, 9]]
    )
    == 35
)
assert (
    count_gold(
        [
            [4],
            [3, 0],
            [5, 1, 1],
            [2, 0, 2, 0],
            [1, 1, 1, 8, 3],
            [5, 3, 4, 8, 2, 8],
            [1, 0, 5, 0, 4, 3, 1],
        ]
    )
    == 30
)
assert (
    count_gold(
        [
            [6],
            [7, 9],
            [3, 8, 3],
            [3, 4, 0, 2],
            [6, 9, 9, 6, 8],
            [3, 7, 0, 8, 2, 2],
            [0, 6, 3, 0, 0, 6, 7],
        ]
    )
    == 49
)
assert (
    count_gold(
        [
            [6],
            [0, 6],
            [3, 0, 7],
            [0, 4, 2, 9],
            [4, 4, 3, 6, 9],
            [3, 1, 0, 5, 9, 0],
            [8, 9, 7, 7, 3, 4, 5],
        ]
    )
    == 50
)
assert (
    count_gold(
        [
            [6],
            [6, 9],
            [7, 1, 4],
            [6, 9, 9, 7],
            [1, 6, 7, 9, 7],
            [5, 7, 2, 6, 0, 9],
            [1, 2, 2, 6, 0, 1, 6],
            [8, 5, 0, 3, 1, 4, 3, 1],
            [9, 6, 4, 1, 1, 9, 3, 7, 9],
            [5, 8, 4, 3, 5, 4, 5, 1, 8, 3],
        ]
    )
    == 66
)
"""
print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
Пример выполнения:

Для пирамиды:


    [1]
   [2, 3]
  [3, 3, 1]
 [3, 1, 5, 4]
[3, 1, 3, 1, 3]
[2, 2, 2, 2, 2, 2]
[5, 6, 4, 5, 6, 4, 3]

    Начинаем с вершины (1).
    Вычисляем максимальную сумму для двух возможных путей (2 и 3).
    Для каждого пути продолжаем вычисление до основания пирамиды.
    Возвращаем максимальную сумму.

Надеюсь, это объяснение поможет лучше понять решение. Если есть еще вопросы или что-то непонятно, пожалуйста, дайте знать!

"""