"""
Как биржевой брокер, специализирующийся на одной сделке, вы стремитесь максимизировать свою прибыль,
покупая акции по более низкой цене и продавая их позже по более высокой цене в течение определенного периода.

Ваша функция должна анализировать колебания цен на акции с течением времени.
Он должен определить наиболее выгодную возможность, рассчитав максимальную потенциальную прибыль,
достижимую в условиях этих колебаний.
Это означает, что нужно найти самую высокую цену для продажи акций после их покупки по самой низкой возможной цене.

Однако если нет возможности получить прибыль (например, когда цена акций постоянно снижается или остается неизменной),
функция должна возвращать ноль, что указывает на отсутствие реальной возможности для прибыльной сделки.
"""

def stock_profit(stock: list[int]) -> int:
    # your code here
    # Вводим переменную для хранения максимальной прибыли
    prof = 0
    # Определяем длину списка акций
    l = len(stock)
    # Цикл для выбора дня покупки
    # Цикл перебирает индексы от 0 до предпоследнего элемента списка (день покупки).
    for b_ind in range(l - 1):
        # Вложенный цикл для выбора дня продажи
        # Вложенный цикл перебирает индексы от дня покупки + 1 до последнего элемента списка (день продажи)
        for s_ind in range(b_ind + 1, l):
            # Вычисляем прибыль для выбранных дней покупки и продажи
            # Для текущих дней покупки и продажи вычисляется прибыль (stock[s_ind] - stock[b_ind]),
            # и если эта прибыль больше текущей максимальной прибыли (prof), то обновляется значение prof.
            prof = max(prof, stock[s_ind] - stock[b_ind])
    # Возвращаем максимальную прибыль
    return prof


print("Example:")
print(stock_profit([3, 1, 3, 4, 5, 1]))

# These "asserts" are used for self-checking
assert stock_profit([2, 3, 4, 5]) == 3
assert stock_profit([3, 1, 3, 4, 5, 1]) == 4
assert stock_profit([4, 3, 2, 1]) == 0
assert stock_profit([6, 2, 1, 2, 3, 2, 3, 4, 5, 4]) == 4
assert stock_profit([1, 1, 1, 2, 1, 1, 1]) == 1
assert stock_profit([4, 3, 2, 1, 2, 1, 2, 1]) == 1
assert stock_profit([1, 1, 1, 1]) == 0

print("You are the best broker here! Click 'Check' to earn cool rewards!")

"""
# Clear
def stock_profit(stock: list) -> int:
    current_maximum = 0                                         # Initialize Variables
    maximum_profit = 0                                          # Initialize Variables
    for price in reversed(stock):                               # Loop over all prices in reversed order as max has to be found before min
        current_maximum = max(price, current_maximum)           # ... if current value is a new max, this will be our new max.
        possible_profit = current_maximum - price               # ... calculate a possible profit
        maximum_profit = max(possible_profit, maximum_profit)   # ... and get the maximum of current possible and max profit  
    return maximum_profit

print("Example:")
print(stock_profit([3, 1, 3, 4, 5, 1]))

assert stock_profit([2, 3, 4, 5]) == 3
assert stock_profit([3, 1, 3, 4, 5, 1]) == 4
assert stock_profit([4, 3, 2, 1]) == 0
assert stock_profit([6, 2, 1, 2, 3, 2, 3, 4, 5, 4]) == 4
assert stock_profit([1, 1, 1, 2, 1, 1, 1]) == 1
assert stock_profit([4, 3, 2, 1, 2, 1, 2, 1]) == 1
assert stock_profit([1, 1, 1, 1]) == 0

print("You are the best broker here! Click 'Check' to earn cool rewards!")

# Creative
stock_profit=p=lambda s:len(s)and max(max(s)-s[0],p(s[1:]))

# Speedy
def stock_profit(stock: list[int]) -> int:
    max_profit = 0
    buy = stock[0]
    for sell in stock:
        profit = sell - buy
        max_profit = max(max_profit, profit)
        if sell < buy:
            buy = sell
    return max_profit


print("Example:")
print(stock_profit([3, 1, 3, 4, 5, 1]))

# These "asserts" are used for self-checking
assert stock_profit([2, 3, 4, 5]) == 3
assert stock_profit([3, 1, 3, 4, 5, 1]) == 4
assert stock_profit([4, 3, 2, 1]) == 0
assert stock_profit([6, 2, 1, 2, 3, 2, 3, 4, 5, 4]) == 4
assert stock_profit([1, 1, 1, 2, 1, 1, 1]) == 1
assert stock_profit([4, 3, 2, 1, 2, 1, 2, 1]) == 1
assert stock_profit([1, 1, 1, 1]) == 0

print("You are the best broker here! Click 'Check' to earn cool rewards!")
"""