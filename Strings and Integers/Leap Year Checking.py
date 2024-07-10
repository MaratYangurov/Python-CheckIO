"""
Проверьте, является ли данный год високосным. Год является високосным, если он делится на 4,
за исключением годов конца века, которые должны делиться на 400.
Это означает, что 2000 год был високосным, а 1900 год - нет.
"""
def is_leap_year(year: int) -> bool:
    # your code here
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


print("Example:")
print(is_leap_year(1891))

# These "asserts" are used for self-checking
assert is_leap_year(2000) == True
assert is_leap_year(1900) == False
assert is_leap_year(2004) == True
assert is_leap_year(2100) == False
assert is_leap_year(2020) == True
assert is_leap_year(2021) == False
assert is_leap_year(1600) == True
assert is_leap_year(1700) == False
assert is_leap_year(1800) == False
assert is_leap_year(2400) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
