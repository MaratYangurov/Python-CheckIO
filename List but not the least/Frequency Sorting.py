"""
Отсортируйте данный список таким образом, чтобы его элементы оказались в порядке убывания частоты их появления,
то есть по количеству раз, которое они появляются в элементах.
Если два элемента имеют одинаковую частоту, они должны оказаться в своем естественном порядке.
Например

Как это используется: Для анализа данных с помощью математической статистики и мат.анализа,
а также для нахождения тенденций и предсказания будущих изменений (систем, явлений и т.д.)
Предусловия:
длина списка <= 100
max number <= 100
"""
from collections.abc import Iterable


def frequency_sorting(numbers: list) -> list:
    # replace this for solution
    res = sorted(numbers, key=lambda x: (-numbers.count(x), x))
    return res

print("Example:")
print(list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])))

# These "asserts" are used for self-checking
assert list(frequency_sorting([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
assert list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])) == [
    4,
    4,
    4,
    3,
    3,
    11,
    11,
    7,
    13,
]

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
# Clear
def checkio(numbers):
    return sorted(sorted(numbers), key=numbers.count, reverse=True)
    
# Creative
def frequency_sorting(numbers):
    return sorted(numbers, key=lambda a: (-numbers.count(a), a))

if __name__ == '__main__':
    print("Example:")
    print(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert frequency_sorting([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Already sorted"
    assert frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]) == [4, 4, 4, 3, 3, 11, 11, 7, 13], "Not sorted"
    assert frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]) == [10, 10, 21, 21, 55, 55, 99, 99], "Reversed"
    print("Coding complete? Click 'Check' to earn cool rewards!")
    

# Speedy
from collections import Counter
from typing import List


def frequency_sorting(numbers: List[int]) -> List[int]:
    count = Counter(numbers)
    numbers.sort(key=lambda x: (-count[x], x))
    return numbers


if __name__ == '__main__':
    print("Example:")
    print(frequency_sorting([1, 2, 3, 4, 5]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert frequency_sorting([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Already sorted"
    assert frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]) == [4, 4, 4, 3, 3, 11, 11, 7, 13], "Not sorted"
    assert frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]) == [10, 10, 21, 21, 55, 55, 99, 99], "Reversed"
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""