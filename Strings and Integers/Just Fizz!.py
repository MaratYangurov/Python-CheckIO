"""
Вы должны написать функцию, которая получает целое положительное число и возвращает "Fizz",
если число делится на 3 (3, 6, 9...), в противном случае преобразует число в строку (2 -> "2").
"""


def checkio(num: int) -> str:
    # your code here
    if num % 3 == 0:
        return "Fizz"
    elif num % 3 == 0.33:
        return "1"
    elif num % 3 == 0.66:
        return "2"
    else:
        return str(num)


print("Example:")
print(checkio(3))

# These "asserts" are used for self-checking
assert checkio(15) == "Fizz"
assert checkio(6) == "Fizz"
assert checkio(10) == "10"
assert checkio(7) == "7"

print("The mission is done! Click 'Check Solution' to earn rewards!")


"""
#Clear
def checkio(num: int) -> str:
    return str(num) if num % 3 else 'Fizz'
    
#Speedy
def checkio(x):
    if x % 3:
        return str(x)
    else:
        return "Fizz"
"""