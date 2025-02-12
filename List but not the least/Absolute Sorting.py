"""
Давайте посмотрим на сортировку. Дан массив с особыми правилами.

Массив (a list) содержит различные числа. Вам необходимо отсортировать их,
но отсортировать на основе абсолютных значений в возрастающем порядке.
Для примера, последовательность (-20, -5, 10, 15) будет отсортирована следующим образом (-5, 10, 15, -20).
Ваша функция должна возвращать список (list) или кортеж (tuple).

Входные данные: Массив чисел как кортеж (tuple).
Выходные данные: Список (list) или кортеж (tuple) (но не генератор) отсортированный по абсолютным значениям чисел.
Дополнение: Результат вашей функции вы увидите как список (list) в панели выводов результатов проверки.
"""

def checkio(values: list) -> list:
    # your code here
    return sorted(values, key=lambda x: abs(x))

print("Example:")
print(checkio([-20, -5, 10, 15]))

# These "asserts" are used for self-checking
assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
def checkio(values: list) -> list:
    return sorted(values, key=abs)
print("Example:")
print(checkio([-20, -5, 10, 15]))
# These "asserts" are used for self-checking
assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]
print("The mission is done! Click 'Check Solution' to earn rewards!")    


checkio = lambda n: sorted(n, key=abs)
# These "asserts" are used for self-checking
assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]
print("The mission is done! Click 'Check Solution' to earn rewards!")  


def checkio(values: list) -> list:
    values.sort(key = lambda x: abs(x))
    return values
# These "asserts" are used for self-checking
assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]
print("The mission is done! Click 'Check Solution' to earn rewards!")  
"""