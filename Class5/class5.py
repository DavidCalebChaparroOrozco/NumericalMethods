# Exercise 3: Quadratic equation
import sys
from numpy import sqrt
'''
Code to show the effect of rounding errors in the solution of a quadratic equation.
'''
from sympy import solveset, S
from sympy.abc import x

# Equation coefficient
a = 1
b = 3000.001
c = 3

# Standard general formula
s1m1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
s2m1 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)

# General formula rewritten
s1m2 = -2*c / (b + sqrt(b**2 - 4*a*c))
s2m2 = -2*c / (b - sqrt(b**2 - 4*a*c))

# Solution obtained with solveset command
s1 , s2 = solveset(a*x**2 + b*x + c)

print(f'Solution 1, Method 1: {s1m1}')
print(f'Solution 2, Method 1: {s2m1}')
print(f'Solution 1, Method 1: {s1m2}')
print(f'Solution 2, Method 2: {s2m2}')
print(f'Solution 1: {s1}')
print(f'Solution 2: {s2}')