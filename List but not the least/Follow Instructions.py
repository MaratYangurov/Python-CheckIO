"""
Вы получили письмо от друга, которого вы не видели и не слышали какое-то время.
В этом письме он дает вам указания о том, как найти скрытое сокровище!
В этой миссии Вы должны следовать данному списку инструкций, которые приведут вас к определенной точке на карте.
Список инструкций - это строка, каждая буква этой строки указывает Вам направление следующего шага.
Буква «f» - указывает на то, что Вам нужно двигаться вперед, «b» - назад, «l» - влево, а «r» - вправо.
То есть, если список Ваших инструкций - «fflff», то Вы должны сделать два шага вперед,
потом один шаг влево, а затем снова переместиться на два шага вперед.
Теперь давайте представим, что Вы находитесь в позиции (0, 0). Продвинувшись вперед, Вы измените свою позицию на (0, 1).
Сделав еще один шаг, она будет (0, 2). Ступив влево, Ваша позиция станет (-1, 2). И после последующих двух шагов вперед Ваши координаты будут (-1, 4).

Ваша цель заключается в том, чтобы найти конечные координаты.
Точно так же, как в приведенном выше примере они были (-1, 4).
"""
def follow(instructions: str) -> tuple[int, int] | list[int]:
    # your code here
    x = 0
    y = 0
    for i in instructions:
        if i == 'f':
            y += 1
        elif i == 'b':
            y -= 1
        elif i == 'l':
            x -= 1
        elif i == 'r':
            x += 1
    return x, y



print("Example:")
print(list(follow("fflff")))

# These "asserts" are used for self-checking
assert list(follow("fflff")) == [-1, 4]
assert list(follow("ffrff")) == [1, 4]
assert list(follow("fblr")) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
# Clear
def follow(instructions):
    c = instructions.count
    return c('r') - c('l'), c('f') - c('b')

if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
    
# Это действительно простое решение. Большое вам спасибо.
# Но он пройдет по строке четыре раза.
# Если длина строки слишком велика, я думаю, это займет много времени.

# Speedy
from collections import Counter
from typing import Tuple

def follow(instructions: str) -> Tuple[int]:
    count = Counter(instructions)
    return (count['r'] - count['l'], count['f'] - count['b'])

if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
"""