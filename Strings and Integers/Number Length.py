"""
Вам дано положительное целое число. Определите сколько цифр оно имеет.
"""


def number_length(value: int) -> int:
    # your code here
    word = str(value)
    count = 0
    for i in word:
        count += 1
    return count


print("Example:")
print(number_length(10))

# These "asserts" are used for self-checking
assert number_length(10) == 2
assert number_length(0) == 1
assert number_length(4) == 1
assert number_length(44) == 2

print("The mission is done! Click 'Check' to earn cool rewards!")

"""
#Clear
def number_length(number: int) -> int:
    return len(str(number))


if __name__ == '__main__':
    print("Example:")
    print(number_length(10))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
    
#Speedy
from bisect import bisect
K = [0, 
     10, 
     100, 
	 1000, 
	 10000, 
	 100000, 
	 1000000,
     10000000, 
	 100000000, 
	 1000000000,
     10000000000]

def number_length(n):
    return bisect(K, n)
"""