"""
У нас есть список логических значений (bool).
Давайте проверим, истинно ли большинство элементов.

Некоторые случаи, о которых стоит упомянуть:
1) пустой список должен возвращать False; 2) если значения True и False равны, функция должна вернуть False.
"""

def is_majority(items: list[bool]) -> bool:
    # your code here
    if items.count(True) > items.count(False):
        return True
    return False


print("Example:")
print(is_majority([True, True, False, True, False]))

# These "asserts" are used for self-checking
assert is_majority([True, True, False, True, False]) == True
assert is_majority([True, True, False]) == True
assert is_majority([True, True, False, False]) == False
assert is_majority([True, True, False, False, False]) == False
assert is_majority([False]) == False
assert is_majority([True]) == True
assert is_majority([]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")


"""
#Clear
def is_majority(items: list) -> bool:
    return sum(items) > len(items) / 2
    
# Speedy
from typing import List


def is_majority(items: List[bool]) -> bool:
    return sum(items) > len(items)//2


if __name__ == '__main__':
    print("Example:")
    print(is_majority([True, True, False, True, False]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_majority([True, True, False, True, False]) == True
    assert is_majority([True, True, False]) == True
    assert is_majority([True, True, False, False]) == False
    assert is_majority([True, True, False, False, False]) == False
    assert is_majority([False]) == False
    assert is_majority([True]) == True
    assert is_majority([]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""