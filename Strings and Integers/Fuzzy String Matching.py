"""
Учитывая две строки и допустимое количество различий в символах, определите, можно ли считать строки примерно равными.
"""
def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
    # your code here
    for i in range(max(len(str1), len(str2))):
        try:
            if str1[i] != str2[i]:
                threshold -= 1
        except IndexError:
            threshold -= 1

    return threshold >= 0



print("Example:")
print(fuzzy_string_match("apple", "appel", 2))

# These "asserts" are used for self-checking
assert fuzzy_string_match("apple", "appel", 2) == True
assert fuzzy_string_match("apple", "bpple", 1) == True
assert fuzzy_string_match("apple", "bpple", 0) == False
assert fuzzy_string_match("apple", "apples", 1) == True
assert fuzzy_string_match("apple", "bpples", 2) == True
assert fuzzy_string_match("apple", "apxle", 1) == True
assert fuzzy_string_match("apple", "pxxli", 3) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
#Clear
from itertools import zip_longest


def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
    
    return sum(i != j for i, j in zip_longest(str1, str2, fillvalue="+")) <= threshold


print("Example:")
print(fuzzy_string_match("apple", "appel", 2))

# These "asserts" are used for self-checking
assert fuzzy_string_match("apple", "appel", 2) == True
assert fuzzy_string_match("apple", "bpple", 1) == True
assert fuzzy_string_match("apple", "bpple", 0) == False
assert fuzzy_string_match("apple", "apples", 1) == True
assert fuzzy_string_match("apple", "bpples", 2) == True
assert fuzzy_string_match("apple", "apxle", 1) == True
assert fuzzy_string_match("apple", "pxxli", 3) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")

# Speedy
from itertools import zip_longest

def fuzzy_string_match(str1: str, str2: str, threshold: int) -> bool:
    return sum(char != sec for char, sec in zip_longest(str1, str2, fillvalue='+')) <= threshold

if __name__ == '__main__':
    print("Example:")
    print(fuzzy_string_match("apple", "appel", 2))

    # These "asserts" are used for self-checking
    assert fuzzy_string_match("apple", "appel", 2) == True
    assert fuzzy_string_match("apple", "bpple", 1) == True
    assert fuzzy_string_match("apple", "bpple", 0) == False
    assert fuzzy_string_match("apple", "apples", 1) == True
    assert fuzzy_string_match("apple", "bpples", 2) == True
    assert fuzzy_string_match("apple", "apxle", 1) == True
    assert fuzzy_string_match("apple", "pxxli", 3) == False

    print("The mission is done! Click 'Check Solution' to earn rewards!")
"""