"""
В заданной строке вам необходимо проверить, идет ли один символ сразу за другим. Если да — верните True, иначе — False.

Если одного из символов нет в данном слове — ваша функция должна вернуть False.
Если два символа поиска одинаковы, ваша функция должна вернуть False.
"""

def goes_after(word: str, first: str, second: str) -> bool:
    # your code here
    first_word = word.find(first)
    second_word = word.find(second)
    if second_word - first_word != 1:
        return False
    return True


print("Example:")
print(goes_after("world", "w", "o"))

# These "asserts" are used for self-checking
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
#Clear
def goes_after(word: str, first: str, second: str) -> bool:
    try:
        return word.index(first) - word.index(second) == -1
    except:
        return False


print("Example:")
print(goes_after("world", "w", "o"))

# These "asserts" are used for self-checking
assert goes_after("world", "w", "o") == True
assert goes_after("world", "w", "r") == False
assert goes_after("world", "l", "o") == False
assert goes_after("list", "l", "o") == False
assert goes_after("", "l", "o") == False
assert goes_after("list", "l", "l") == False
assert goes_after("world", "d", "w") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")

#Speedy
def goes_after(word: str, first: str, second: str) -> bool:
    return f"{first}{second}" in word
"""