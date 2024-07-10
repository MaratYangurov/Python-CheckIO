"""
Вы можете посмотреть упрощенную версию этой миссии First Word (simplified).
Текущее задание чуть более сложное, поскольку в нем кроме букв английского алфавита присутствуют и другие символы.

Дана строка и нужно найти ее первое слово.

При решении задачи обратите внимание на следующие моменты:

В строке могут встречатся точки и запятые
Строка может начинаться с буквы или, к примеру, с пробела или точки
В слове может быть апостроф и он является частью слова
Весь текст может быть представлен только одним словом и все
"""
def first_word(text: str) -> str:
    # your code here
    punctuations = ',.'
    new_s = ""
    for char in text:
        if char in punctuations:
            new_s += ' '
        else:
            new_s += char
    new_s = new_s.replace(" - ", " ")
    new_s = new_s.split()
    return new_s[0]


print("Example:")
print(first_word("Hello world"))

# These "asserts" are used for self-checking
assert first_word("Hello world") == "Hello"
assert first_word(" a word ") == "a"
assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"
assert first_word("... and so on ...") == "and"
assert first_word("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
# Clear
import re


def first_word(text: str) -> str:
    return re.search("([\w']+)", text).group(1)

# Speedy
def first_word(text: str) -> str:
    i = 0
    while i < len(text) and text[i] in ',. ':
        i += 1
    j = i
    while j < len(text) and text[j] not in ',. ':
        j += 1
    return text[i:j]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""