"""
Вам нужно посчитать, сколько непустых строк имеет данный текст.

Пустая строка – это строка без символов или строка, содержащая только пробелы.
"""

def non_empty_lines(text: str) -> int:
    # your code here
    t = 0
    for i in text.split('\n'):
        if len(i.strip()) > 0:
            t += 1
    return t


print("Example:")
print(non_empty_lines("\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\n            "))

# These "asserts" are used for self-checking
assert non_empty_lines("one simple line\n") == 1
assert non_empty_lines("") == 0
assert non_empty_lines("\nonly one line\n            ") == 1
assert (
    non_empty_lines(
        "\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\n            "
    )
    == 3
)

print("The mission is done! Click 'Check Solution' to earn rewards!")


"""
# Clear
def non_empty_lines(text: str) -> int:
    return sum(bool(line.strip()) for line in text.splitlines())


if __name__ == '__main__':
    print("Example:")
    print(non_empty_lines('one simple line\n'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert non_empty_lines('one simple line\n') == 1
    assert non_empty_lines('') == 0
    assert non_empty_lines('\nonly one line\n            ') == 1
    assert non_empty_lines('''
Lorem ipsum dolor sit amet,

consectetur adipiscing elit
Nam odio nisi, aliquam
            ''') == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
    
# Мне не приходило в голову, что line.strip() 
# для пустых строк будет разрешаться в ноль, 
# если для него задан тип bool, но это имеет смысл. Хороший.

# Speedy
def non_empty_lines(text: str) -> int:
    return sum(bool(line.split()) for line in text.splitlines())

if __name__ == '__main__':
    print("Example:")
    print(non_empty_lines('one simple line\n'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert non_empty_lines('one simple line\n') == 1
    assert non_empty_lines('') == 0
    assert non_empty_lines('\nonly one line\n            ') == 1
    assert non_empty_lines('''
Lorem ipsum dolor sit amet,

consectetur adipiscing elit
Nam odio nisi, aliquam
            ''') == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""