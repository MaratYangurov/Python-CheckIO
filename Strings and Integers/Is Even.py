"""
Проверить является ли число четным или нет.
Ваша функция должна возвращать True если число четное, и False если число не четное.
"""

def is_even(num: int) -> bool:
    if num % 2 == 0:
        return True
    return False

print("Example:")
print(is_even(2))

# These "asserts" are used for self-checking
assert is_even(2) == True
assert is_even(5) == False
assert is_even(0) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
# Clear
def is_even(num: int) -> bool:
    return num & 1 == 0


if __name__ == '__main__':
    print("Example:")
    print(is_even(2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")

# Speedy    
def is_even(num: int) -> bool:
    # your code here
    return not(num & 1)

    # think it faster than num %2 

if __name__ == '__main__':
    print("Example:")
    print(is_even(2))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_even(2) == True
    assert is_even(5) == False
    assert is_even(0) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""