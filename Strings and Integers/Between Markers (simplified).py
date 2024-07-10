"""
Вам дана строка и два маркера (начальный и конечный).
Вам необходимо найти текст, заключенный между двумя этими маркерами. Но есть несколько важных условий.

Начальный и конечный маркеры всегда разные.
Начальный и конечный маркеры всегда размером в один символ.
Начальный и конечный маркеры всегда есть в строке и идут один за другим.
"""

def between_markers(text: str, start: str, end: str) -> str:
    # your code here
    text_start = text.index(start)
    text_end = text.index(end)

    return text[text_start+1: text_end]


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

# These "asserts" are used for self-checking
assert between_markers("What is >apple<", ">", "<") == "apple"
assert between_markers("What is [apple]", "[", "]") == "apple"
assert between_markers("What is ><", ">", "<") == ""
assert between_markers("[an apple]", "[", "]") == "an apple"

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
#Clear
def between_markers(text: str, begin: str, end: str) -> str:
    #returns substring between two given markers
    
    return text[text.index(begin)+1:text.index(end)]
    
#Speedy
def between_markers(text, begin, end):
    i = text.find(begin) + 1
    j = text.find(end, i)
    return text[i:j]
"""