"""
Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд),
затем перемножить эту сумму и последний элемент исходного массива.
Не забудьте, что первый элемент массива имеет индекс 0.

Для пустого массива результат всегда 0 (ноль).
"""

def checkio(array: list[int]) -> int:
    # your code here
    count = 0
    if array == []:
        return 0
    else:
        for i in array[::2]:
            count += i

        return count * array[-1]


print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
# Clear
def checkio(array):
    
    # sums even-indexes elements and multiply at the last  
    if len(array) == 0: return 0
    return sum(array[0::2]) * array[-1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "Empty"
    
# Speedy
def checkio(array):
    
    # sums even-indexes elements and multiply at the last
    return sum(array[0::2])*array[-1] if 0 < len(array) else 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "Empty"
"""