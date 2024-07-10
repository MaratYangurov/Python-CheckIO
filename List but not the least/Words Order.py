"""
У вас есть текст и последовательность слов.
Вам нужно проверить, появляются ли слова в последовательности в том же порядке, что и в данном тексте.

Задачи, которые вы должны решить при решении этой задачи:
    слово из последовательности отсутствует в тексте - ваша функция должна вернуть False;
    любое слово может встречаться в тексте более одного раза - используйте только первое;
    два слова в заданной последовательности одинаковы - ваша функция должна вернуть False;
    условие чувствительно к регистру, что означает 'hi' и 'Hi' это два разных слова;
    текст включает только английские буквы и пробелы.
Ввод: Два аргумента. Первый - заданный текст в виде строки (str), второй - список элементов list в виде строк (str).
Вывод: Логическое значение (bool).
"""
def words_order(text: str, words: list) -> bool:
    # your code here
    # Множество по условию
    result = {i for i in text.split() if i in words}
    # функция возвращает true, если результат сортировки result по ключу text.index совпадает со списком слов words.
    return sorted(result, key=text.index) == words

print("Example:")
print(words_order("hi world im here", ["world", "here"]))

# These "asserts" are used for self-checking
assert words_order("hi world im here", ["world", "here"]) == True
assert words_order("hi world im here", ["here", "world"]) == False
assert words_order("hi world im here", ["world"]) == True
assert words_order("hi world im here", ["world", "here", "hi"]) == False
assert words_order("hi world im here", ["world", "im", "here"]) == True
assert words_order("hi world im here", ["world", "hi", "here"]) == False
assert words_order("hi world im here", ["world", "world"]) == False
assert words_order("hi world im here", ["country", "world"]) == False
assert words_order("hi world im here", ["wo", "rld"]) == False
assert words_order("", ["world", "here"]) == False
assert words_order("hi world world im here", ["world", "world"]) == False
assert (
    words_order("hi world world im here hi world world im here", ["world", "here"])
    == True
)

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
# Clear
def words_order(text, words):
    text_words = {w for w in text.split() if w in words}
    return list(sorted(text_words, key=text.index)) == words
    
# Speedy
def words_order(text: str, words: list) -> bool:
    # A word that appears twice make this simple.
    if len(set(words)) != len(words):
        return False
    # Look for words indexes with a simple iteration on text words.
    words = {word: -1 for word in words}  # A dict remembers insertion order.
    for n, text_word in enumerate(text.split()):
        if text_word in words and words[text_word] == -1:
            words[text_word] = n
    # Make sure all words are in the text and indexes are increasing.
    last = -1
    for index in words.values():
        if index <= last:
            return False
        last = index
    return True
"""