"""
Дана строка и нужно найти ее первое слово.

Строка состоит только из английских символов и пробелов.
В начале и в конце строки пробелов нет.
"""
def first_word(text: str) -> str:
    # your code here
    word = text.split()
    return word[0]


print("Example:")
print(first_word("Hello world"))

# These "asserts" are used for self-checking
assert first_word("Hello world") == "Hello"
assert first_word("a word") == "a"
assert first_word("greeting from CheckiO Planet") == "greeting"
assert first_word("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
#Clear
def first_word(text):
    index = text.find(" ")
    return text[:index] if index != -1 else text
    
#Speedy
def first_word(text: str) -> str:
    i = 0
    while i < len(text) and text[i] != ' ':
        i += 1
    return text[:i]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""