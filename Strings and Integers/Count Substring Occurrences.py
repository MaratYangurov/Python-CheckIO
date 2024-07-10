"""
This function should take a main string and a substring as inputs and return the number of occurrences of the substring within the main string.
It should not be case-sensitive and may overlap.
"""

def count_occurrences(main_str: str, sub_str: str) -> int:
    ind = res = 0
    main_str = main_str.lower()
    sub_str = sub_str.lower()
    while (ind := main_str.find(sub_str, ind)) != -1:
        res += 1
        ind += 1

    return res


print("Example:")
print(count_occurrences("hello world hello", "hello"))

# These "asserts" are used for self-checking
assert count_occurrences("hello world hello", "hello") == 2
assert count_occurrences("Hello World hello", "hello") == 2
assert count_occurrences("hello", "world") == 0
assert count_occurrences("hello world hello world hello", "world") == 2
assert count_occurrences("HELLO", "hello") == 1
assert count_occurrences("appleappleapple", "appleapple") == 2
assert count_occurrences("HELLO WORLD", "WORLD") == 1
assert count_occurrences("hello world hello", "o w") == 1
assert count_occurrences("apple apple apple", "apple") == 3
assert count_occurrences("apple Apple apple", "apple") == 3
assert count_occurrences("apple", "APPLE") == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")


"""
#Clear
def count_occurrences(main_str: str, sub_str: str) -> int:
    return sum(
        main_str[i : i + len(sub_str)].lower() == sub_str.lower()
        for i in range(len(main_str))
    )
    
#Speedy
import re

def count_occurrences(main_str: str, sub_str: str) -> int:
    return len(re.findall(f'(?=({sub_str.lower()}))', main_str.lower()))


print("Example:")
print(count_occurrences("hello world hello", "hello"))

# These "asserts" are used for self-checking
assert count_occurrences("hello world hello", "hello") == 2
assert count_occurrences("Hello World hello", "hello") == 2
assert count_occurrences("hello", "world") == 0
assert count_occurrences("hello world hello world hello", "world") == 2
assert count_occurrences("HELLO", "hello") == 1
assert count_occurrences("HELLO WORLD", "WORLD") == 1
assert count_occurrences("hello world hello", "o w") == 1
assert count_occurrences("apple apple apple", "apple") == 3
assert count_occurrences("apple Apple apple", "apple") == 3
assert count_occurrences("apple", "APPLE") == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
"""