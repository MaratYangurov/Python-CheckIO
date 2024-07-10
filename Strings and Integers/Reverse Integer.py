"""
Поменяйте местами цифры заданного целого числа. Например, 1234 должно стать 4321.
Для отрицательных целых чисел знак должен оставаться впереди; например, -123 становится -321.
"""
def reverse_digits(num: int) -> int:
    # your code here
    if num < 0:
        modul_num = abs(num)
        modul_num_str = str(modul_num)
        revers_num_str = modul_num_str[::-1]
        revers_num = int(revers_num_str)
        revers_num = revers_num * (-1)
        return revers_num
    else:
        modul_num = abs(num)
        modul_num_str = str(modul_num)
        revers_num_str = modul_num_str[::-1]
        revers_num = int(revers_num_str)
        return revers_num


print("Example:")
print(reverse_digits(32))

# These "asserts" are used for self-checking
assert reverse_digits(1234) == 4321
assert reverse_digits(0) == 0
assert reverse_digits(-123) == -321
assert reverse_digits(5) == 5
assert reverse_digits(-9) == -9
assert reverse_digits(100) == 1
assert reverse_digits(-100) == -1
assert reverse_digits(54321) == 12345
assert reverse_digits(1111) == 1111
assert reverse_digits(987654321) == 123456789

print("The mission is done! Click 'Check Solution' to earn rewards!")


"""
# Claer
def reverse_digits(num: int) -> int:
    
    return int(''.join(reversed(str(num)))) if num >= 0 else -int(''.join(reversed(str(-num))))


print("Example:")
print(reverse_digits(32))

# These "asserts" are used for self-checking
assert reverse_digits(1234) == 4321
assert reverse_digits(0) == 0
assert reverse_digits(-123) == -321
assert reverse_digits(5) == 5
assert reverse_digits(-9) == -9
assert reverse_digits(100) == 1
assert reverse_digits(-100) == -1
assert reverse_digits(54321) == 12345
assert reverse_digits(1111) == 1111
assert reverse_digits(987654321) == 123456789

print("The mission is done! Click 'Check Solution' to earn rewards!")

# Speedy
def reverse_digits(num: int) -> int:

    return int(str(num)[::-1]) if num>=0 else -1*int(str(abs(num))[::-1])
      

print("Example:")
print(reverse_digits(32))

# These "asserts" are used for self-checking
assert reverse_digits(1234) == 4321
assert reverse_digits(0) == 0
assert reverse_digits(-123) == -321
assert reverse_digits(5) == 5
assert reverse_digits(-9) == -9
assert reverse_digits(100) == 1
assert reverse_digits(-100) == -1
assert reverse_digits(54321) == 12345
assert reverse_digits(1111) == 1111
assert reverse_digits(987654321) == 123456789

print("The mission is done! Click 'Check Solution' to earn rewards!")
"""