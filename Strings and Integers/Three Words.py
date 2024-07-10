"""
Давайте научим наших роботов отличать слова от чисел.

Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.
"""


def checkio(words: str) -> bool:
    # add your code here
    count = 0
    for w in words.split():
        if w.isalpha():
            count += 1
            if count == 3:
                return True
        else:
            count = 0

    return False


print("Example:")
print(checkio("Hello World hello"))

# These "asserts" are used for self-checking
assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
assert checkio("Hi") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
#Clear
def checkio(words):
    succ = 0
    for word in words.split():
        succ = (succ + 1)*word.isalpha()
        if succ == 3: return True
    else: return False
# I'm just learning and I usually come to the solutions to see how more experienced people do it. 
# I often look at comments in these examples for further explanation/insight, but often times there is not much info. 
# So, I just thought I'd annotate this with some of my key takeaways from this, to help out the next person.
# Boolean can be treated as integers (true=1, false=0)
#'Return' acts as a break in for loops (and other such operations)
# You can use else statements with for loops. 
#They are executed when the for loop ends naturally (as in not from a 'break')    

#Speedy
import re

def checkio(words):
    return True if re.search('\D+\s\D+\s\D+', words) else False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"

"""