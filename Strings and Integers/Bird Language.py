"""
У Стефана есть друг -- маленькая робо-птичка. Какое-то время он пытался научить её говорить по-английски. И вот сегодня она произнесла первое слово: «hieeelalaooo». Звучит как «hello», но слишком уж много гласных. Стефан попросил Николу помочь с этим, и тот изучил, как птица меняет слова. Теперь нам осталось только написать модуль для перевода с птичьего.

Птичка меняет слова по следующим правилам:
- после каждой согласной буквы она добавляет случайную гласную букву (l ⇒ la or le);
- после каждой гласной буквы она добавляет две таких же буквы (a ⇒ aaa);
Гласные буквы == "aeiouy".

Вам дана птичья фраза как несколько слов, разделёных пробелами (каждая пара слов разделена одним пробелом).
Птичка не знает ничего о знаках пунктуации и использует только буквы. Все слова даны в нижнем регистре.
Необходимо перевести эту птичью песню в понятную простым роботам фразу.

Входные данные: Птичья фраза как строка (string).

Выходные данные: Перевод как строка (string).

Связь с реальной жизнью: Этот простой «шифр» похож на тот, который используют дети для своего «птичьего» языка.
Но теперь-то вы легко взломаете их хитрости.

Предусловия: re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase)
Фраза всегда имеет перевод.
"""


def translation(text: str) -> str:
    # your code here
    letters = "aeiouy"
    new = ''
    index = 0
    while index < len(text):
        if text[index] == ' ':
            new += text[index]
        elif text[index] not in letters and text[index + 1] in letters:
            new += text[index]
            index += 1
        elif text[index] in letters:
            if text[index:index + 3] == text[index] * 3:
                new += text[index]
                index += 2
        index += 1
    return new


print("Example:")
print(translation("hieeelalaooo"))

# These "asserts" are used for self-checking
assert translation("hieeelalaooo") == "hello"
assert translation("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translation("aaa bo cy da eee fe") == "a b c d e f"
assert translation("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")


"""
# Clear
VOWELS = "aeiouy"

def translation(phrase):
    output = ""
    c = 0
    
    while c < len(phrase):
        output += phrase[c]
        if phrase[c] in VOWELS:
            c = c + 3
        elif phrase[c] == ' ':
            c = c + 1
        else:
            c = c + 2

    return output
    
# Speedy
translate=lambda s:s and s[0]+translate(s[1+(s[0]!=' ')+(s[0]in'aeiouy'):])
"""