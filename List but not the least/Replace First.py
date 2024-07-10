"""
В данном списке первый элемент должен стать последним. Пустой список или список из одного элемента не должен измениться.m
"""
from collections.abc import Iterable


def replace_first(items: list) -> Iterable:
    # your code here
    new_items = items[1:]
    if len(items) <= 1:
        return items
    for i in items:
        new_items.append(items[0])
        return new_items

# These "asserts" are used for self-checking
print("Example:")
print(list(replace_first([1, 2, 3, 4])))

assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
assert replace_first([1]) == [1]
assert replace_first([]) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")


"""
# Clear
# Change items IN-PLACE.
def replace_first(items: list) -> list:
    if items:
        items.append(items.pop(0))
    return items

# Slices
def replace_first(items: list) -> list:
    return items[1:] + items[:1]

# collections.deque have an useful method: rotate.
from collections import deque
def replace_first(items: list) -> deque:
    items = deque(items)
    items.rotate(-1)
    return items
    
# Из другого решения, которое я «упростил», я хотел бы добавить четвертое:
# python import functools as fn import numpy as np replace_first = fn.partial(np.roll, shift=-1)

# Speedy
def replace_first(lst):
    if len(lst):
        lst.append(lst.pop(0))
    return lst
"""
