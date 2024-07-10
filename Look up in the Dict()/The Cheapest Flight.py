"""
«Нам нужно долететь домой как можно дешевле, чтобы больше денег осталось на подарки.
Тётя Лида просила сыров разных, а Вася хотел машинку новую.
Я уже довольно долго смотрю на расписание, и мне начинает казаться, что некоторые самолёты летают зря.»
На входе вы получаете расписание самолётов в виде списка,
каждый элемент которого — это цена прямого воздушного соединения двух городов
(список из 3 элементов: первые два — названия городов в виде строк, и третий — цена перелёта).
Самолёты летают в обе стороны и цена в обе стороны одинаковая.
Есть вероятность, что соединения между городами может и не быть.
Найдите цену самого дешёвого перелёта для городов, которые переданы 2-м и 3-м аргументами.
Если перелет невозможен, верните 0
Входные данные: 3 аргумента: расписание перелётов в виде списка списков, город вылета, город назначения как строки.
Выходные данные: Лучшая цена как целое число.
"""

def cheapest_flight(data, start, stop):
    stack, found, best = [(start, 0)], False, 1e9
    while stack:
        path, price = stack.pop()
        if path[-1] == stop:
            best, found = min(best, price), True
            continue
        for a, b, p in data:
            stack += [(path+b, price+p)]*(a == path[-1] and b not in path)
            stack += [(path+a, price+p)]*(b == path[-1] and a not in path)
    return best*found

print("Example:")
print(cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C"))

# These "asserts" are used for self-checking
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C") == 70
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A") == 70
)
assert (
    cheapest_flight(
        [
            ["A", "C", 40],
            ["A", "B", 20],
            ["A", "D", 20],
            ["B", "C", 50],
            ["D", "C", 70],
        ],
        "D",
        "C",
    )
    == 60
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F") == 0
)
assert (
    cheapest_flight(
        [["A", "B", 10], ["A", "C", 15], ["B", "D", 15], ["C", "D", 10]], "A", "D"
    )
    == 25
)

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
# Speedy
from typing import List
# 生成矩阵
def matrix_genetor(vex_num):
    data_matrix = []
    for i in range(vex_num):
        one_list = []
        for j in range(vex_num):
            one_list.append(9999)
        data_matrix.append(one_list)
    return data_matrix

c_index = lambda x: ord(str(x)) - ord("A")

def cheapest_flight(costs: List, a: str, b: str) -> int:
    nums_vertex = 0
    for cost in costs: nums_vertex = max(c_index(cost[0]), c_index(cost[1])) + 1
    matrix = matrix_genetor(nums_vertex)
    for cost in costs:
        u, v, c = cost
        matrix[c_index(u)][c_index(v)] = c
        matrix[c_index(v)][c_index(u)] = c

    for k in range(nums_vertex):
        for i in range(nums_vertex):
            for j in range(nums_vertex):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    result = matrix[c_index(a)][c_index(b)]
    return 0 if result == 9999 else result


if __name__ == '__main__':
    print("Example:")
    print(cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'A',
 'C'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'A',
 'C') == 70
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'C',
 'A') == 70
    assert cheapest_flight([['A', 'C', 40],
  ['A', 'B', 20],
  ['A', 'D', 20],
  ['B', 'C', 50],
  ['D', 'C', 70]],
 'D',
 'C') == 60
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['D', 'F', 900]],
 'A',
 'F') == 0
    assert cheapest_flight([['A', 'B', 10],
  ['A', 'C', 15],
  ['B', 'D', 15],
  ['C', 'D', 10]],
 'A',
 'D') == 25
    print("Coding complete? Click 'Check' to earn cool rewards!")
    
    
# Creative
from typing import List


def cheapest_flight_1(costs, a: str, b: str):
    if a == b: return 0
    else:
        costs += [[s[1],s[0],s[2]] for s in costs]
        try: return min(s[2] + cheapest_flight_1([t for t in costs if a not in t], s[1], b) for s in costs if a==s[0] )
        except ValueError: return 2e30

def cheapest_flight(costs, a,b):
    return 0 if cheapest_flight_1(costs,a,b)>=2e30 else cheapest_flight_1(costs,a,b)

if __name__ == '__main__':
    print("Example:")
    print(cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'A',
 'C'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'A',
 'C') == 70
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'C',
 'A') == 70
    assert cheapest_flight([['A', 'C', 40],
  ['A', 'B', 20],
  ['A', 'D', 20],
  ['B', 'C', 50],
  ['D', 'C', 70]],
 'D',
 'C') == 60
    assert cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['D', 'F', 900]],
 'A',
 'F') == 0
    assert cheapest_flight([['A', 'B', 10],
  ['A', 'C', 15],
  ['B', 'D', 15],
  ['C', 'D', 10]],
 'A',
 'D') == 25
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""