"""
Эта функция должна взять список строк и определить самый длинный общий префикс среди всех строк.
Если общего префикса нет, он должен вернуть пустую строку.
"""
def longest_prefix(arr: list[str]) -> str:
    # your code here
    first_res = arr.pop() #выносим отдельно последний элемент list
    len_first_res = len(first_res) #его количество
    while arr: #Запускаем бесконечный цикл
        sec_res, i = arr.pop(), 0 #выносим отдельно еще один элемент списка и сопостасляем щетчик
        # запускаем цикл, где сопоставляем счетчик с минимальном количеством символов и проверяем одинаковые ли символы в отдельных словах
        while i < min(len_first_res, len(sec_res)) and first_res[i] == sec_res[i]:
            #если да то добавляем значение счетчику
            i += 1
        #Если значение переменной i равно нулю (то есть если длина наименьшей строки равна нулю), возвращается пустая строка "".
        #Если значение переменной i не равно нулю (то есть если длина наименьшей строки не равна нулю), программа продолжает свое выполнение.
        #not (l:= i) - проверяет, не равно ли значение переменной l нулю. Если l равно нулю (то есть i равно нулю),
        # выражение становится истинным (True), а если l не равно нулю (то есть i не равно нулю), выражение становится ложным (False).
        if not (len_first_res := i):
            return ""
    return first_res[:len_first_res]


print("Example:")
print(longest_prefix(["flower", "flow", "flight"]))

# These "asserts" are used for self-checking
assert longest_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_prefix(["dog", "racecar", "car"]) == ""
assert longest_prefix(["apple", "application", "appetizer"]) == "app"
assert longest_prefix(["a"]) == "a"
assert longest_prefix(["", "b"]) == ""
assert longest_prefix(["same", "same", "same"]) == "same"
assert longest_prefix(["mismatch", "mister", "miss"]) == "mis"
assert longest_prefix(["alphabet", "alpha", "alphadog"]) == "alpha"
assert longest_prefix(["book", "boot", "booster"]) == "boo"
assert longest_prefix(["short", "shore", "shot"]) == "sho"

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
# Clear
def longest_prefix(arr: list[str]) -> str:
    # your code here
    s = arr.pop()    
    for i in range(len(s)+1):
        if not all(s[:i] in x for x in arr):
            return s[:i-1]
    return s[:i]


print("Example:")
print(longest_prefix(["flower", "flow", "flight"]))

# These "asserts" are used for self-checking
assert longest_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_prefix(["dog", "racecar", "car"]) == ""
assert longest_prefix(["apple", "application", "appetizer"]) == "app"
assert longest_prefix(["a"]) == "a"
assert longest_prefix(["", "b"]) == ""
assert longest_prefix(["same", "same", "same"]) == "same"
assert longest_prefix(["mismatch", "mister", "miss"]) == "mis"
assert longest_prefix(["alphabet", "alpha", "alphadog"]) == "alpha"
assert longest_prefix(["book", "boot", "booster"]) == "boo"
assert longest_prefix(["short", "shore", "shot"]) == "sho"

print("The mission is done! Click 'Check Solution' to earn rewards!")

# Speedy
def longest_prefix(arr: list[str]) -> str:

    res = arr.pop()
    l = len(res)
    while arr:
        sec, i = arr.pop(), 0
        while i < min(l, len(sec)) and res[i] == sec[i]: i += 1
        if not (l:= i): return ""
        
    return res[:l]


print("Example:")
print(longest_prefix(["flower", "flow", "flight"]))

# These "asserts" are used for self-checking
assert longest_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_prefix(["dog", "racecar", "car"]) == ""
assert longest_prefix(["apple", "application", "appetizer"]) == "app"
assert longest_prefix(["a"]) == "a"
assert longest_prefix(["", "b"]) == ""
assert longest_prefix(["same", "same", "same"]) == "same"
assert longest_prefix(["mismatch", "mister", "miss"]) == "mis"
assert longest_prefix(["alphabet", "alpha", "alphadog"]) == "alpha"
assert longest_prefix(["book", "boot", "booster"]) == "boo"
assert longest_prefix(["short", "shore", "shot"]) == "sho"

print("The mission is done! Click 'Check Solution' to earn rewards!")
"""
