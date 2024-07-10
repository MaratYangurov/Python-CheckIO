"""
"На протяжении веков, левши страдали от дискриминации в мире, созданном для правшей."
Santrock, John W. (2008). Motor, Sensory, and Perceptual Development.

"Большинство людей (70-95%) правши, меньшинство (5-30 %) левши,
и неопределеное число людей вероятно лучше всего охарактеризовать, как "симметричные"."
Scientific American. www.scientificamerican.com

Один робот был занят простой задачей:
объединить последовательность строк в одно выражение для создания инструкции по обходу корабля.
Но робот был левша и зачастую шутил и запутывал своих друзей правшей.

Дана последовательность строк. Вы должны объединить эти строки в блок текста, разделив изначальные строки запятыми.
В качестве шутки над праворукими роботами, вы должны заменить все вхождения слова "right" на слова "left",
даже если это часть другого слова. Все строки даны в нижнем регистре.
"""
def left_join(phrases: tuple) -> str:
    # your code here
    phrases_list = []
    phrases_str = ''
    for i in phrases:
        i = i.replace('right', 'left')
        phrases_list.append(i)
    phrases_str = ','.join(phrases_list)
    return phrases_str

print("Example:")
print(left_join(("left", "right", "left", "stop")))

# These "asserts" are used for self-checking
assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
assert left_join(("brightness wright",)) == "bleftness wleft"
assert left_join(("enough", "jokes")) == "enough,jokes"

print("The mission is done! Click 'Check Solution' to earn rewards!")


"""
# Clear
def left_join(phrases):
    return ','.join(map(lambda x:x.replace('right','left'),phrases))

# Speedy
def left_join(phrases):
    return ",".join(phrases).replace("right", "left")

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
"""