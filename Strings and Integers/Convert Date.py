"""
Эта функция должна принимать строку даты в формате дд/мм/гггг и конвертировать ее в формат гггг-мм-дд.
Если входные данные имеют неправильный формат, функция должна вернуть сообщение об ошибке «Ошибка: неверная дата».
"""

import datetime


def convert_date(date: str) -> str:
    try:
        dd, mm, yyyy = date.split("/")
    except ValueError:
        return "Error: Invalid date."

    try:
        D = datetime.date(int(yyyy), int(mm), int(dd))
    except ValueError:
        return "Error: Invalid date."

    res = D.isoformat()
    if res != f"{yyyy}-{mm}-{dd}":
        return "Error: Invalid date."

    return res


print("Example:")
print(convert_date("01/01/2023"))

# These "asserts" are used for self-checking
assert convert_date("25/12/2021") == "2021-12-25"
assert convert_date("01/01/2000") == "2000-01-01"
assert convert_date("15/06/1995") == "1995-06-15"
assert convert_date("29/02/2020") == "2020-02-29"
assert convert_date("10/10/2010") == "2010-10-10"
assert convert_date("31/05/1985") == "1985-05-31"
assert convert_date("07/08/1960") == "1960-08-07"
assert convert_date("02/09/1999") == "1999-09-02"
assert convert_date("30/04/1975") == "1975-04-30"
assert convert_date("29/02/2019") == "Error: Invalid date."
assert convert_date("30/04/1975/1") == "Error: Invalid date."

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
# Clear
import datetime
def convert_date(date: str) -> str:
    try:
        date_obj = datetime.datetime.strptime(date, '%d/%m/%Y')
        return date_obj.strftime('%Y-%m-%d')
    except:
        return "Error: Invalid date."

# Speedy
import datetime

def convert_date(date: str) -> str:
    try:
        return datetime.datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d")  
    except ValueError:
        return "Error: Invalid date."




print("Example:")
print(convert_date("01/01/2023"))

# These "asserts" are used for self-checking
assert convert_date("25/12/2021") == "2021-12-25"
assert convert_date("01/01/2000") == "2000-01-01"
assert convert_date("15/06/1995") == "1995-06-15"
assert convert_date("29/02/2020") == "2020-02-29"
assert convert_date("10/10/2010") == "2010-10-10"
assert convert_date("31/05/1985") == "1985-05-31"
assert convert_date("07/08/1960") == "1960-08-07"
assert convert_date("02/09/1999") == "1999-09-02"
assert convert_date("30/04/1975") == "1975-04-30"
assert convert_date("29/02/2019") == "Error: Invalid date."
assert convert_date("30/04/1975/1") == "Error: Invalid date."

print("The mission is done! Click 'Check Solution' to earn rewards!")
"""