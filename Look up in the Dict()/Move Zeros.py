"""
Вам дан список целых чисел. Переместите все нули в списке в конец.
Порядок ненулевых элементов не должен меняться.
"""
from typing import Iterable


def move_zeros(items: list[int]) -> Iterable[int]:
    # your code here
    res = []
    for i in items:
        if i != 0:
            res.append(i)
    for i in range(len(items)-len(res)):
        res.append(0)
    return res



print("Example:")
print(list(move_zeros([0, 1, 0, 3, 12])))

# These "asserts" are used for self-checking
assert list(move_zeros([0, 1, 0, 3, 12])) == [1, 3, 12, 0, 0]
assert list(move_zeros([0])) == [0]

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
# Clear
def move_zeros(items: list[int]) -> list[int]:
    return [v for v in items if v] + [0] * items.count(0)

print("Example:")
print(move_zeros([0, 1, 0, 3, 12]))

assert move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
assert move_zeros([0]) == [0]

print("The mission is done! Click 'Check Solution' to earn rewards!")


# Creative
move_zeros = __import__('functools').partial(sorted, key=bool, reverse=True)


# Speedy
def move_zeros(items: list[int]) -> list[int]:
    a, b = [],[]
    for j in items:
        if j :
            a.append(j)
        else:
            b.append(j)
    return a + b


print("Example:")
print(move_zeros([0, 1, 0, 3, 12]))

assert move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
assert move_zeros([0]) == [0]

print("The mission is done! Click 'Check Solution' to earn rewards!")
"""