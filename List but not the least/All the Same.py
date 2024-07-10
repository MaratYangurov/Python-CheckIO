"""
В этой миссии Вам надо определить, все ли элементы массива равны.
"""
from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here
    new_elements = set(elements)
    return False if len(new_elements) > 1 else True

print("Example:")
print(all_the_same([1, 1, 1]))

# These "asserts" are used for self-checking
assert all_the_same([1, 1, 1]) == True
assert all_the_same([1, 2, 1]) == False
assert all_the_same([1, "a", 1]) == False
assert all_the_same([1, 1, 1, 2]) == False
assert all_the_same([]) == True
assert all_the_same([1]) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
# Clear
# В этой миссии вам предстоит проверить, все ли элементы в данном списке равны.
# Вход: Список.
# Выход: Бул.

from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    return len(set(elements)) <= 1

if __name__ == '__main__':
    assert all_the_same([1, 1, 1])
    assert not all_the_same([1, 2, 1])
    assert all_the_same(['a', 'a', 'a'])
    assert all_the_same([])
    assert all_the_same([1])

# когда вы создаете набор из списка, вы удаляете все дубликаты.
# set() работает с пустыми списками, возвращая пустой набор.
# длина пустого набора равна 0.

# Speedy
from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    return all(elements[i]==elements[i+1] for i in range(len(elements)-1))

if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""