'''
Требуется обратить порядок букв в каждом слове предоставленной строки, так чтобы слова остались на своих местах.
'''

def backward_string_by_word(text: str) -> str:
    # your code here
    return ' '.join(word[::-1] for word in text.split(' '))

print("Example:")
print(backward_string_by_word("hello   world"))

# These "asserts" are used for self-checking
assert backward_string_by_word("") == ""
assert backward_string_by_word("world") == "dlrow"
assert backward_string_by_word("hello world") == "olleh dlrow"
assert backward_string_by_word("hello   world") == "olleh   dlrow"
assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
# Clear
def backward_string_by_word(text):
    return ' '.join(word[::-1] for word in text.split(' '))
# Большой! Но как метод join() может вставить необходимое количество пространства? Вопрос по делу

# Speedy
def backward_string_by_word(text: str) -> str:
    return ' '.join([i[::-1] for i in text.split(' ')])

if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""