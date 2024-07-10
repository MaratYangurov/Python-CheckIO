"""
Отсортируйте целые числа по порядку.
А вот положение нулей менять не следует.
"""
from collections.abc import Iterable


def except_zero(items: list) -> list:
    # your code here
    # Создаем список res, который содержит индексы всех элементов, равных нулю.
    res = [i for i, v in enumerate(items) if v == 0]
    # Создаем список res_2, который содержит все НЕнулевые элементы из items, отсортированные по возрастанию.
    res_2 = sorted(filter(lambda x: x > 0, items))
    # Для каждого индекса i из списка res, вставляем ноль на позицию i в список res_2.
    for i in res:
        res_2.insert(i, 0)

    return res_2


print("Example:")
print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

# These "asserts" are used for self-checking
assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
assert list(except_zero([0, 0])) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
# Clear
from typing import Iterable

def except_zero(items: list) -> Iterable:
    # создать итератор для отсортированного ненулевого элемента
    it = iter(sorted(e for e in items if e))
    # вставить 0
    yield from [next(it) if e else 0 for e in items]

if __name__ == '__main__':
    print("Example:")
    print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
    assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
    assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
    assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
    assert list(except_zero([0, 0])) == [0, 0]
    print("Coding complete? Click 'Check' to earn cool rewards!")


# Creative
def except_zero(L):
    s = iter(sorted(filter(None, L)))
    return [x and next(s) for x in L]


# Speedy
from typing import Iterable, List


def except_zero(items: List[int]) -> Iterable[int]:
    sorted_non_zeros = sorted((item for item in items if item))
    i = 0
    for item in items:
        if not item:
            yield 0
            continue
        yield sorted_non_zeros[i]
        i += 1


if __name__ == '__main__':
    print("Example:")
    print(list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
    assert list(except_zero([0, 2, 3, 1, 0, 4, 5])) == [0, 1, 2, 3, 0, 4, 5]
    assert list(except_zero([0, 0, 0, 1, 0])) == [0, 0, 0, 1, 0]
    assert list(except_zero([4, 5, 3, 1, 1])) == [1, 1, 3, 4, 5]
    assert list(except_zero([0, 0])) == [0, 0]
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""