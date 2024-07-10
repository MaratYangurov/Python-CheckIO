"""
Ваша функция должна создать список списков, представляющий собой двумерную сетку с
заданным количеством строк и столбцов.

Эта сетка должна содержать целые числа (int) от начала до начала + строки * столбцы - 1
в порядке возрастания, но элементы каждой строки с нечетным индексом должны быть перечислены
в порядке убывания, чтобы при чтении в порядке возрастания числа шли зигзагом.
через двумерную сетку.
"""
def create_zigzag(rows: int, cols: int, start: int = 1) -> list[list[int]]:
    # your code here
    result = [] # Создали первичный список
    for row in range(0, rows): # Идем циклом по количествам строк rows
        row_list = []  # Создали вторичный список
        for col in range(0, cols): # Идем циклом по количествам колонок cols - они же тупо значения
            row_list.append(start) # Добавляем во вторичный список значиния начиная от start, ровно столько сколько = cols
            start += 1 # Двигаем счетчик
        result.append(row_list) # Добавили в первичный список вторичные внутри цикла
    u = [] # Создали финальный список
    for i in range(len(result)): # идем по количесве вложенных списков в списке result
        if i % 2 == 0: # Если число четное
            u.append(result[i]) # Добавляем просто вложенный список
        else: # Если число не четное
            u.append(result[i][::-1])# Добавляем вложенный список вывирнув наизнанку значения
    return u



print("Example:")
print(create_zigzag(3, 5))

# These "asserts" are used for self-checking
assert create_zigzag(3, 5) == [[1, 2, 3, 4, 5], [10, 9, 8, 7, 6], [11, 12, 13, 14, 15]]
assert create_zigzag(5, 1) == [[1], [2], [3], [4], [5]]
assert create_zigzag(3, 3, 5) == [[5, 6, 7], [10, 9, 8], [11, 12, 13]]

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
# Clear
from typing import List
from itertools import count, islice

def create_zigzag(rows: int, cols: int, start: int = 1) -> List[List[int]]:
    it = count(start)
    return [list(islice(it, cols))[::(-1)**row] for row in range(rows)]
    

# Speedy
from typing import List
def create_zigzag(rows: int, cols: int, start: int = 1) -> List[List[int]]:
    numbers=range(start,start+rows*cols)
    array=[]
    for row in range(rows):
        array.append(list(numbers[row*cols:(row+1)*cols]))
        if row % 2 == 1:
            array[-1].reverse()
    return array
"""