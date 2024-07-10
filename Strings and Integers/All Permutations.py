"""
Учитывая строку, верните все возможные перестановки ее символов, отсортированные в алфавитном порядке.
"""
from collections.abc import Iterable


def string_permutations(word: str) -> Iterable[str]:
    # your code here
    if len(word) == 1 or len(word) == 0:
        return word
    result = []
    for index, char in enumerate(word):
        word_without_char = remove_char_from_word_by_index(word, index)
        list_sub_permutations = string_permutations(word_without_char)
        result += [char + x for x in list_sub_permutations]
    return result

def remove_char_from_word_by_index(word, delete_index):
    if delete_index == 0:
        return word[1:]
    elif delete_index == len(word)-1:
        return word[:-1]
    else:
        return word[:delete_index] + word[delete_index+1:]


print("Example:")
print(list(string_permutations("abcd")))

# These "asserts" are used for self-checking
assert list(string_permutations("ab")) == ["ab", "ba"]
assert list(string_permutations("abc")) == ["abc", "acb", "bac", "bca", "cab", "cba"]
assert list(string_permutations("a")) == ["a"]
assert list(string_permutations("abcd")) == [
    "abcd",
    "abdc",
    "acbd",
    "acdb",
    "adbc",
    "adcb",
    "bacd",
    "badc",
    "bcad",
    "bcda",
    "bdac",
    "bdca",
    "cabd",
    "cadb",
    "cbad",
    "cbda",
    "cdab",
    "cdba",
    "dabc",
    "dacb",
    "dbac",
    "dbca",
    "dcab",
    "dcba",
]

print("The mission is done! Click 'Check Solution' to earn rewards!")


"""
Разберем код по строчкам:

```python
from collections.abc import Iterable
```
Эта строка импортирует `Iterable` из модуля `collections.abc`. В данном случае это не обязательно, потому что функция `string_permutations` возвращает список, который уже является итерируемым объектом.

```python
def string_permutations(s: str) -> Iterable[str]:
```
Здесь определяется функция `string_permutations`, которая принимает строку `s` и возвращает итерируемый объект, содержащий все перестановки этой строки.

```python
    if len(s) < 2: return [s]
```
Если длина строки `s` меньше двух (т.е. она пустая или состоит из одного символа), функция сразу возвращает список, содержащий саму строку. Это база для рекурсивного подхода.

```python
    all = []
```
Создается пустой список `all`, в который будут добавляться все перестановки строки.

```python
    for i, char in enumerate(s):
```
Запускается цикл по каждому символу строки `s`, где `i` — индекс символа, а `char` — сам символ.

```python
        remaining_chars = s[:i] + s[i + 1:]
```
Создается строка `remaining_chars`, которая содержит все символы строки `s`, кроме текущего символа `char`.

```python
        for perm in string_permutations(remaining_chars):
```
Рекурсивно вызывается функция `string_permutations` для строки `remaining_chars`. Для каждой перестановки `perm` из этого вызова выполняется следующий шаг.

```python
            all.append(char + perm)
```
К текущему символу `char` добавляется каждая перестановка `perm`, и результат добавляется в список `all`.

```python
    return sorted(all)
```
После завершения всех рекурсивных вызовов возвращается отсортированный список `all`, содержащий все перестановки строки `s`.

```python
print("Example:")
print(list(string_permutations("abcd")))
```
Пример использования функции: выводятся все перестановки строки `"abcd"` в виде отсортированного списка.

### Весь код целиком:
```python
from collections.abc import Iterable

def string_permutations(s: str) -> Iterable[str]:
    if len(s) < 2: return [s]
    all = []
    for i, char in enumerate(s):
        remaining_chars = s[:i] + s[i + 1:]
        for perm in string_permutations(remaining_chars):
            all.append(char + perm)
    return sorted(all)
    
print("Example:")
print(list(string_permutations("abcd")))
```

### Как работает функция:

1. **База рекурсии**: Если строка состоит из одного символа или пуста, возвращается список, содержащий саму строку.
2. **Рекурсивный шаг**: Для каждого символа строки:
   - Убирается текущий символ, формируется оставшаяся часть строки.
   - Вызывается функция `string_permutations` для этой оставшейся части строки.
   - Каждая полученная перестановка соединяется с текущим символом и добавляется в список `all`.
3. **Возврат результата**: Возвращается отсортированный список всех перестановок.

"""