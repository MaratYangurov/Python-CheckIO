"""
Данная последовательность должна быть «сжата» таким образом, чтобы вместо двух (или более) одинаковых элементов,
стоящих друг за другом, в результирующей последовательности должен быть только один.
"""
from collections.abc import Iterable


def compress(items: list) -> list:
    # your code here
    for ind, val in enumerate(items):
        if not ind or val != items[ind - 1]:
            yield val


print("Example:")
print(list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])))

# These "asserts" are used for self-checking
assert list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])) == [
    5,
    4,
    5,
    6,
    5,
    7,
    8,
    0,
]
assert list(compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])) == [1, 2, 1]
assert list(compress([7, 7])) == [7]
assert list(compress([])) == []
assert list(compress([1, 2, 3, 4])) == [1, 2, 3, 4]
assert list(compress([9, 9, 9, 9, 9, 9, 9])) == [9]
assert list(compress([9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9])) == [9, 0, 9]

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
# Clear
from itertools import groupby

def compress(items):
    for key, _ in groupby(items): yield key
    
# Speedy 
compress= lambda x: [x[i] for i in range(len(x)) if i==0 or x[i]!=x[i-1]]


if __name__ == '__main__':
    print("Example:")
    print(list(compress([
  5, 5, 5,
  4, 5, 6,
  6, 5, 5,
  7, 8, 0,
  0])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(compress([
  5, 5, 5,
  4, 5, 6,
  6, 5, 5,
  7, 8, 0,
  0])) == [5, 4, 5, 6, 5, 7, 8, 0]
    assert list(compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])) == [1, 2, 1]
    assert list(compress([7, 7])) == [7]
    assert list(compress([])) == []
    assert list(compress([1, 2, 3, 4])) == [1, 2, 3, 4]
    assert list(compress([9, 9, 9, 9, 9, 9, 9])) == [9]
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""
