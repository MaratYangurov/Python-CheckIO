"""
Дан непустой массив целых чисел (X).
В этой задаче вам нужно вернуть массив, состоящий только из неуникальных элементов данного массива.
Для этого необходимо удалить все уникальные элементы (которые присутствуют в данном массиве только один раз).
Для решения этой задачи не меняйте оригинальный порядок элементов.
Пример: [1, 2, 3, 1, 3], где 1 и 3 неуникальные элементы и результат будет [1, 3, 1, 3].
Как это используется:
Эта задача поможет вам понять, как манипулировать массивами.
Это полезный базис для решения более сложных задач.
Также эта идея может быть легко обобщена для реальных задач.
Для примера: если вам необходимо очистить статистику от редко встречающихся элементов (шум).
"""
from collections.abc import Iterable


def checkio(data: list[int]) -> Iterable[int]:
    # your code here
    set_data = set(data)
    for i in  set_data:
        if data.count(i) == 1:
            data.remove(i)
    return data

print("Example:")
print(list(checkio([1, 2, 3, 1, 3])))

# These "asserts" are used for self-checking
assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3]
assert list(checkio([1, 2, 3, 4, 5])) == []
assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5]
assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9]
assert list(checkio([2, 2, 3, 2, 2])) == [2, 2, 2, 2]
assert list(checkio([10, 20, 30, 10])) == [10, 10]
assert list(checkio([7])) == []
assert list(checkio([0, 1, 2, 3, 4, 0, 1, 2, 4])) == [0, 1, 2, 4, 0, 1, 2, 4]
assert list(checkio([99, 98, 99])) == [99, 99]
assert list(checkio([0, 0, 0, 1, 1, 100])) == [0, 0, 0, 1, 1]
assert list(checkio([0, 0, 0, -1, -1, 100])) == [0, 0, 0, -1, -1]

print("The mission is done! Click 'Check Solution' to earn rewards!")


"""
# Clear
checkio=lambda d:[x for x in d if d.count(x)>1]

# Creative
checkio = lambda d: list(filter(lambda i: d.count(i) - 1, d))

# Speedy
def checkio(data):
    from collections import Counter
    nonunique = Counter(data) - Counter(set(data))
    return [x for x in data if x in nonunique]
"""