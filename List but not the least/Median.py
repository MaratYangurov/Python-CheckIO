"""
Медиана — это числовое значение, которое делит сортированый массив чисел на нижнюю и верхнюю половины.
В сортированом массиве с нечётным числом элементов медиана — это число в середине массива.
Для массива с чётным числом элементов, где нет одного элемента точно посередине,
медиана — это среднее значение двух чисел, находящихся в середине массива.
В этой задаче дан непустой массив натуральных чисел.
Вам необходимо найти медиану данного массива.

Если ты хочешь больше попрактиковаться с подобным заданием, попробуй миссию Middle Characters.

Входные данные: Массив как список (list) чисел (int).

Выходные данные: Медиана как число (int, float).
Как это используется: Медиана находит свое применение в статистике и теории вероятности,
и особенно важна для ассиметричного распределения.
Для примера: мы хотим узнать среднее доход населения -- 100 человек получают $100 в месяц и 10 человек получают $1,000,000.
Если мы возьмем среднее арифметическое, то получим $91,000.
Это довольно странное число, не показывающее истинного положения дел.
В этом случае медиана будет равна $100, что станет для нас более полезной величиной и покажет более правдоподобную картину.
"""

def checkio(data: list[int]) -> int | float:
    # replace this for solution
    data = sorted(data)
    if len(data) % 2 != 0:
        num = data[(len(data)-1)//2]
        return num
    else:
        num = data[((len(data)-2)//2):((len(data)+2)//2)]

        return sum(num)/2

print("Example:")
print(checkio([3, 6, 20, 99, 10, 15]))

# These "asserts" are used for self-checking
assert checkio([1, 2, 3, 4, 5]) == 3
assert checkio([3, 1, 2, 5, 3]) == 3
assert checkio([1, 300, 2, 200, 1]) == 2
assert checkio([3, 6, 20, 99, 10, 15]) == 12.5
assert checkio([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5
assert checkio([0, 7, 1, 8, 4, 9, 5, 6, 2, 3]) == 4.5
assert checkio([33, 56, 62]) == 56
assert checkio([21, 56, 84, 82, 52, 9]) == 54
assert checkio([100, 1, 1, 1, 1, 1, 1]) == 1
assert checkio([64, 6, 92, 7, 70, 5]) == 35.5

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
# Clear
def checkio(data):
    data.sort()
    half = len(data) // 2
    return (data[half] + data[~half]) / 2
    
    
# Speedy
# Find the k'th-smallest value in a, worst case O(n)
# Skip the first d elements and consider only the next n
def select(a, d, n, k):
    if n <= 5:
        return sorted(a[d:d+n])[k]

    # Find median of medians of 5
    medians = [sorted(a[i:i+5])[2] for i in range(d, d+n-4, 5)]
    m = len(medians)
    median = select(medians, 0, m, m // 2)

    # Partition around the median.
    # a[d:i]     <= median
    # a[j+1:d+n] >= median
    i, j = d, d+n-1
    while i <= j:
        while a[i] < median: i += 1
        while a[j] > median: j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    if d+k < i: return select(a, d, i-d, k)
    else:       return select(a, i, n+d-i, k+d-i)

def checkio(data):
    n = len(data)
    if n % 2 == 1:
        return select(data, 0, n, n//2)
    else:
        return 0.5 * (select(data, 0, n, n//2-1) + select(data, 0, n, n//2))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
"""