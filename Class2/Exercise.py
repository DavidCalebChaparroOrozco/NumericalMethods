# Division and Square-root
"""
Write a function called divide_or_square that takes one argument (a number),
and returns the square root of that number if it divisible by 5, returns its
remainder if it is not divisible by 5. For example, if you pass 10 as an
argument, then your function should return 3.16 as the square root of 10.
"""
import math

def divide_or_square(number):
    if number <= 0:
        return print('No se puede dividir por 0')
    elif number % 5 == 0:
        return math.sqrt(number)
    else:
        return number % 5

print('divide_or_square is: '+ str(divide_or_square(0)))