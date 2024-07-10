"""
Вам дан текст в котором нужно просуммировать числа, но только разделенные пробелом.
Если число является частью слова, то его суммировать не нужно.

Текст состоит из чисел, пробелов и букв английского алфавита.
"""
def sum_numbers(text: str) -> int:
    # your code here
    count = 0
    for i in text.split():
        if i.isdigit():
            count += int(i)
    return count


print("Example:")
print(sum_numbers("hi"))

# These "asserts" are used for self-checking
assert sum_numbers("hi") == 0
assert sum_numbers("who is 1st here") == 0
assert sum_numbers("my numbers is 2") == 2
assert (
    sum_numbers(
        "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
    )
    == 3755
)
assert sum_numbers("5 plus 6 is") == 11
assert sum_numbers("") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
#Clear
sum_numbers = lambda text: sum(int(word) for word in text.split() if word.isdigit())

#Speedy
def sum_numbers(text: str) -> int:
    return sum(map(int, filter(str.isdigit, text.split())))
"""
