"""
Вам дана последовательность файлов в виде строк.
Вам нужно отсортировать эту последовательность по расширению файла.
Файлы с одинаковым расширением (или без него) следует отсортировать по имени.

Некоторые возможные случаи:
• Имя файла не может быть пустой строкой;
• Порядок сортировки: файлы без имени, файлы без расширения, файлы с именем и расширением;
• Имя файла .config или config. это все имя с пустым расширением;
• Имя файла, например, str1.str2.str3, имеет расширение str3 и имя str1.str2;
• Имя файла, например .str1.str2, имеет расширение str2 и имя .str1.
"""
def sort_by_ext(files: list[str]) -> list[str]:
    # your code here

    return sorted(files, key = lambda file:
                [(b, a) if a else (a, b) for (a, b) in [file.rsplit('.', 1)]])


print("Example:")
print(sort_by_ext(["1.cad", "1.bat", "1.aa"]))

# These "asserts" are used for self-checking
assert sort_by_ext(["1.cad", "1.bat", "1.aa"]) == ["1.aa", "1.bat", "1.cad"]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", "2.bat"]) == [
    "1.aa",
    "1.bat",
    "2.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".bat"]) == [
    ".bat",
    "1.aa",
    "1.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.bat", ".aa", ".bat"]) == [
    ".aa",
    ".bat",
    "1.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.", "1.aa"]) == ["1.", "1.aa", "1.cad"]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", "1.aa.doc"]) == [
    "1.aa",
    "1.bat",
    "1.cad",
    "1.aa.doc",
]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".aa.doc"]) == [
    "1.aa",
    "1.bat",
    "1.cad",
    ".aa.doc",
]

print("The mission is done! Click 'Check Solution' to earn rewards!")