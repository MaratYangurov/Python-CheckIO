"""
У вас есть число и нужно определить какая цифра из этого числа является наибольшей.
"""

def max_digit(value: int) -> int:
    # your code here
    digit = 0
    value = str(value)
    for i in value:
        if int(i) > digit:
            digit = int(i)
    return digit


print("Example:")
print(max_digit(10))

# These "asserts" are used for self-checking
assert max_digit(0) == 0
assert max_digit(52) == 5
assert max_digit(634) == 6
assert max_digit(1) == 1
assert max_digit(10000) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
#Clear
max_digit = lambda number: int(max(str(number)))

#Speedy
def max_digit(number: int) -> int:
    return max(map(int, str(number)))
"""