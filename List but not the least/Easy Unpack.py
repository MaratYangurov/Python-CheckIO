"""
Ваша цель сейчас — создать функцию, которая принимает на вход кортеж и возвращает кортеж из 3 элементов:
первого, третьего и второго с конца элементов заданного кортежа.

Важно отметить, что вам нужно использовать индекс для извлечения элементов из кортежа.
Обратите внимание, нумерация индексов начинается с 0, не с 1.
Это означает, что если вы хотите получить первый элемент из кортежа elements, вам нужен elements[0], а если второй — elements[1].
"""

def easy_unpack(elements: tuple) -> tuple:
    # your code here
    return (elements[0], elements[2], elements[-2])


print("Example:")
print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

# These "asserts" are used for self-checking
assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
assert easy_unpack((6, 3, 7)) == (6, 7, 3)

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
# Clear
from operator import itemgetter
easy_unpack = itemgetter(0, 2, ~1)

# Очень лаконично и умно использовать itemgetter!
# Использование побитового «нет», равного 1, для представления -2 слишком умно и запутывает цель программы.
# Более подробная информация для тех, кто менее знаком с двоичным представлением, используя 8 бит: 1 = b00000001;
# -2 = b11111110; ~1 = b11111110;
# или проще ~1 == -2
# Однако в качестве обучающего упражнения мне удалось найти побитовый оператор not ;) Молодец!

# Speedy
def easy_unpack(elements):
    return (elements[0], elements[2], elements[-2])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')
"""