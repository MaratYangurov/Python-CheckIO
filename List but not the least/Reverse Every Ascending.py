"""
Создайте и верните новый Iterable, который содержит те же элементы, что и заданные элементы списка,
но с обратным порядком элементов внутри каждой максимальной строго возрастающей подпоследовательности.
Эта функция не должна изменять содержимое исходного списка.
"""

from collections.abc import Iterable


def reverse_ascending(items: list[int]) -> Iterable[int]:
    # Создаем пустой список result, который будет хранить результат.
    result: list[int] = []
    for elem in items:
        # Проверяем, пуст ли result или elem меньше или равен элементу в result на позиции point.
        #     if not result проверяет, пуст ли список result.
        #     elem <= result[point] проверяет, меньше ли elem или равен элементу в result на позиции point.
        #     Если одно из этих условий истинно, point устанавливается в len(result).
        if not result or elem <= result[point]:
            point = len(result)
        # Вставляем элемент elem в список result на позицию point.
        result.insert(point, elem)

    return result

print("Example:")
print(list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])))

# These "asserts" are used for self-checking
assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [
    10,
    7,
    5,
    4,
    8,
    7,
    2,
    3,
    1,
]
assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([])) == []
assert list(reverse_ascending([1])) == [1]
assert list(reverse_ascending([1, 1])) == [1, 1]
assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]

print("The mission is done! Click 'Check Solution' to earn rewards!")


"""
# Clear
#to_list = lambda f: lambda *args, **kwargs: list(f(*args, **kwargs))

#@to_list # Outputs doesn't have to be lists in "Check" tests.
def reverse_ascending(iterable):
    ascending = []
    for elem in iterable:
        if ascending and ascending[-1] >= elem:
            yield from reversed(ascending)
            ascending = []
        ascending.append(elem)
    yield from reversed(ascending)
    
# Speedy
def reverse_ascending(items):
    for s in range(1,len(items)): 
        if items[s] <= items[s-1]:
            return items[:s][::-1]+reverse_ascending(items[s:])
    return items[::-1]


if __name__ == '__main__':
    print("Example:")
    print(reverse_ascending([1, 2, 3, 4, 5]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
    assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([])) == []
    assert list(reverse_ascending([1])) == [1]
    assert list(reverse_ascending([1, 1])) == [1, 1]
    assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""