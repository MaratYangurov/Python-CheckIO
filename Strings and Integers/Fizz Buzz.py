"""
"Fizz buzz" это игра со словами, с помощью которой мы будем учить наших роботов делению. Давайте обучим компьютер.

Вы должны написать функцию, которая принимает положительное целое число и возвращает:
"Fizz Buzz", если число делится на 3 и 5;
"Fizz", если число делится на 3;
"Buzz", если число делится на 5;
Число, как строку для остальных случаев.
"""


def checkio(num: int) -> str:
    # your code here
    if num % 3 == 0 and num % 5 == 0:
        return "Fizz Buzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else:
        return str(num)


print("Example:")
print(checkio(15))

# These "asserts" are used for self-checking
assert checkio(15) == "Fizz Buzz"
assert checkio(6) == "Fizz"
assert checkio(10) == "Buzz"
assert checkio(7) == "7"

print("The mission is done! Click 'Check Solution' to earn rewards!")


"""
#Clear
#Your optional code here
#You can import some modules or create additional functions


def checkio(number):
    if number % 15 == 0:
        return 'Fizz Buzz'
    if number % 5 == 0:
        return 'Buzz'
    if number % 3 == 0:
        return 'Fizz'
    return str(number)

#Some hints:
#Convert a number in the string with str(n)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "7 is divisible by 5"
    assert checkio(7) == "7", "15 is not divisible by 3 or 5"
    
#Speedy
#Your optional code here
#You can import some modules or create additional functions


def checkio(number):
    if number % 3 == 0:
        result = 'Fizz'
        if number % 5 == 0:
            result += ' Buzz'
    elif number % 5 == 0:
        result = 'Buzz'
    else:
        result = str(number)

    
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.

    #replace this for solution
    return result

#Some hints:
#Convert a number in the string with str(n)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
"""