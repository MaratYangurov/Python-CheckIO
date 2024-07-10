"""
Дана последовательность строк. Вам нужно определить наиболее часто встречаемую строку в последовательности.
"""

def most_frequent(data: list[str]) -> str:
    # your code here
    # Создаем множество уникальных значений списка data
    data_set = set(data)
    # Перебираем множество и смотрим количество букв в списке. Затем создаем список букв
    index_data= [data.count(i) for i in data_set]
    # Формируем словать где key- это числа, а value- это буквы
    data_dict = {key: value for key, value in zip(index_data, data_set)}
    # Возвращаем  значениие value, которое максимально по ключу
    return data_dict[max(data_dict)]


print("Example:")
print(most_frequent(["a", "b", "c", "a", "b", "a"]))

# These "asserts" are used for self-checking
assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
# Speedy
def most_frequent(data):
    return max(set(data), key=data.count)
    
# Clear
from statistics import mode as most_frequent
"""