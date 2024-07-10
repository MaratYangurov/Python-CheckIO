"""
Не все элементы важны. Вам нужно удалить из список все элементы до указаного.
На примере мы имеем список [1, 2, 3, 4, 5] где нужно было удалить все элементы до 3 - 1 и 2 соответственно.

Есть два ньюанса: (1) если в списке нет элемента до которого нужно удалить остальные элементы, то список не должен измениться.
(2) если list пустой, то он должен остаться пустым.

Входные данные: Список и элемент до которого нужно удалить другие элементы.
Выходные данные: Набор значений (кортеж, список, итератор ...).
"""
from collections.abc import Iterable


def remove_all_before(items: list, border: int) -> list:
    # your code here
    check_items = []
    if items == []:
        return []
    elif border not in items:
        return items
    else:
        check_index = items.index(border)
        return items[check_index:]


print("Example:")
print((remove_all_before([1, 1, 2, 2, 3, 3], 2)))

# These "asserts" are used for self-checking
assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
assert list(remove_all_before([], 0)) == []
assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
    7,
]

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
# Creative
remove_all_before=lambda i,b:b in i and i[i.index(b):] or i


# Clear
def remove_all_before(items, border):
    try:
        return items[items.index(border):]
    except ValueError:
        return items


# Speedy
from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    # your code here
    
    return items[items.index(border):] if border in items else items


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""