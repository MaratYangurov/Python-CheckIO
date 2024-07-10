"""
Эта функция должна принимать на вход неотрицательное целое число и возвращать факториал этого числа.
Факториал неотрицательного целого числа n — это произведение всех положительных целых чисел, меньших или равных n.
"""

def factorial(n: int) -> int:
    # your code here
    count = 1


    for i in range(2, n+1):
        count *= i
    return count


print("Example:")
print(factorial(4))

# These "asserts" are used for self-checking
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(10) == 3628800
assert factorial(15) == 1307674368000

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
#Clear
def factorial(n: int) -> int:
    return 1 if n==0 or n==1 else n*factorial(n-1)


print("Example:")
print(factorial(4))

# These "asserts" are used for self-checking
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(10) == 3628800
assert factorial(15) == 1307674368000

print("The mission is done! Click 'Check Solution' to earn rewards!")

#Speedy
def factorial(n: int) -> int:
    
    return __import__('math').prod(range(1,n+1))
"""