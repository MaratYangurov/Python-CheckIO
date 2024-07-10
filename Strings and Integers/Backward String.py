"""
Верните данную строку в перевернутом виде.
"""
def backward_string(val: str) -> str:
    ret_string = val[::-1]
    return ret_string

print("Example:")
print(backward_string("val"))

# These "asserts" are used for self-checking
assert backward_string("val") == "lav"
assert backward_string("") == ""
assert backward_string("ohho") == "ohho"
assert backward_string("123456789") == "987654321"

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
#Clear
backward_string = lambda val: val[::-1]

#Speedy
def backward_string(val: str) -> str:
    return val[::-1]


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""