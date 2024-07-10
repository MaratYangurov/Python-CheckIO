"""
1. Сделаем нашу функцию более привычной. Пусть он принимает некоторый аргумент arg.

2. Вернуть значение аргумента без каких-либо изменений.
"""
# Taken from mission Empty Function

# write your code here
def func(arg):
    a = arg
    return a


print("Example:")
print(func(3))

# These "asserts" are used for self-checking
assert func(3) == 3
assert func("string") == "string"
assert func(True) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")