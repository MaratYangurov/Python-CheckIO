"""
Определите, является ли данное целое число положительным, отрицательным или нулевым, и верните соответствующую строку:
«положительную», «отрицательную» или «ноль».
"""
def determine_sign(num: int) -> str:
    # your code here
    if num == 0:
        return "zero"
    elif num > 0:
        return "positive"
    else:
        return "negative"


print("Example:")
print(determine_sign(11))

# These "asserts" are used for self-checking
assert determine_sign(5) == "positive"
assert determine_sign(0) == "zero"
assert determine_sign(-10) == "negative"
assert determine_sign(1) == "positive"
assert determine_sign(-1) == "negative"
assert determine_sign(999) == "positive"
assert determine_sign(-1000) == "negative"
assert determine_sign(123456789) == "positive"
assert determine_sign(-987654321) == "negative"
assert determine_sign(2) == "positive"

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
#Clear
def determine_sign(num: int) -> str:
    if num == 0: return 'zero'
    if num > 0: return 'positive'
    return 'negative'
    
#Speedy
def determine_sign(num: int) -> str:
    return 'positive' if num > 0 else 'negative' if num < 0 else 'zero'


print("Example:")
print(determine_sign(11))

# These "asserts" are used for self-checking
assert determine_sign(5) == "positive"
assert determine_sign(0) == "zero"
assert determine_sign(-10) == "negative"
assert determine_sign(1) == "positive"
assert determine_sign(-1) == "negative"
assert determine_sign(999) == "positive"
assert determine_sign(-1000) == "negative"
assert determine_sign(123456789) == "positive"
assert determine_sign(-987654321) == "negative"
assert determine_sign(2) == "positive"

print("The mission is done! Click 'Check Solution' to earn rewards!")
"""