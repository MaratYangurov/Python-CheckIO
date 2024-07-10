"""
Не все элементы важны. Здесь вам нужно удалить все элементы после заданного из последовательности.
Для иллюстрации у нас есть последовательность [1, 2, 3, 4, 5], и нам нужно удалить все элементы, следующие после 3 — это 4 и 5.
Здесь у нас есть два крайних случая:
    – если режущий элемент не найден, то последовательность действий менять не следует;
    – если последовательность пуста, то она должна оставаться пустой.
"""
from collections.abc import Iterable

def remove_all_after(items: list[int], border: int) -> Iterable[int]:
    # your code here
    new_items = []
    for i in items:
        if i != border:
            new_items.append(i)
        elif i == border:
            new_items.append(i)
            break
    return new_items



print("Example:")
print(list(remove_all_after([1, 1, 2, 2, 3, 3], 2)))

# These "asserts" are used for self-checking
assert list(remove_all_after([1, 2, 3, 4, 5], 3)) == [1, 2, 3]
assert list(remove_all_after([1, 1, 2, 2, 3, 3], 2)) == [1, 1, 2]
assert list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)) == [1, 1, 2]
assert list(remove_all_after([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
assert list(remove_all_after([], 0)) == []
assert list(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7]

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
# Clear
def remove_all_after(items: list, border: int) -> list:
    try:
        return items[: items.index(border) + 1]
    except ValueError:
        return items
        
# Speedy
from typing import Iterable, List

def remove_all_after(items: List, border: int) -> Iterable:
    for item in items:
        yield item
        if item == border:
            return


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_after([1, 2, 3, 4, 5], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_after([1, 2, 3, 4, 5], 3)) == [1, 2, 3]
    assert list(remove_all_after([1, 1, 2, 2, 3, 3], 2)) == [1, 1, 2]
    assert list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)) == [1, 1, 2]
    assert list(remove_all_after([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_after([], 0)) == []
    assert list(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""
