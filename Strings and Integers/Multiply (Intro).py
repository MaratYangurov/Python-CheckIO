"""
Это вводная миссия, целью которой является показать как решать задачи на CheckiO или как получить максимум от этого.
Если хотите узнать, как получить максимум от CheckiO, смотрите наш пост "From Basic to Advance usage".

Итак, это самая простая миссия. Напишите функцию, которая будет получать 2 числа и возвращать результат произведения этих чисел.
"""

def mult_two(a: int, b: int) -> int:
    c = a * b
    return c


print("Example")
print(mult_two(1, 2))

assert mult_two(3, 2) == 6
assert mult_two(0, 1) == 0

print("The first mission is done! Click 'Check' to earn cool rewards!")