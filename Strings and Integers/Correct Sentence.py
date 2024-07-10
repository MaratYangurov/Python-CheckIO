"""
На вход Вашей функции будет передано одно предложение.
Необходимо вернуть его исправленную копию так, чтобы оно всегда начиналось с большой буквы и заканчивалось точкой.

Обратите внимание на то, что не все исправления необходимы.
Если предложение уже заканчивается на точку, то добавлять еще одну не нужно, это будет ошибкой
"""

def correct_sentence(text: str) -> str:
    # your code here
    text_1 = text[0].capitalize()
    text_sum = text_1 + text[1:]
    text_2 = text_sum.split('.')
    text_3 = ''.join(text_2)
    return f'{text_3}.'



print("Example:")
print(correct_sentence("greetings, friends"))

# These "asserts" are used for self-checking
assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
#Clear
def correct_sentence(text: str) -> str:   
    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")
#The last term ("." if text[-1] != "." else "") is clean and clear. 
#However I would like to suggest another option "."*(text[-1] != ".")

#Speedy
def correct_sentence(text: str) -> str:
    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")

if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""
