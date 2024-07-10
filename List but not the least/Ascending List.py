"""
Определите, является ли последовательность элементов возрастающей,
так что каждый из ее элементов строго больше предыдущего элемента (а не просто равен ему).
Пустая последовательность считается возрастающей.
"""

def is_ascending(items: list[int]) -> bool:
    # your code here
    num = -100
    if items == []:
        return True
    for i in items:
        if num < i:
            num = i

        else:
            return False
    return True


print("Example:")
print(is_ascending([-5, 10, 99, 123456]))

# These "asserts" are used for self-checking
assert is_ascending([-5, 10, 99, 123456]) == True
assert is_ascending([99]) == True
assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
assert is_ascending([]) == True
assert is_ascending([1, 1, 1, 1]) == False
assert is_ascending([1, 3, 3, 5]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
# Clear
from typing import Iterable

def is_ascending(items: Iterable[int]) -> bool:
    return all(items[i] < items[i+1] for i in range(len(items)-1))

if __name__ == '__main__':
    print("Example:")
    print(is_ascending([-5, 10, 99, 123456]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_ascending([-5, 10, 99, 123456]) == True
    assert is_ascending([99]) == True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
    assert is_ascending([]) == True
    assert is_ascending([1, 1, 1, 1]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
    
# Speedy
def is_ascending(items):
    return all(items[i] < items[i+1] for i in range(len(items) - 1))
"""