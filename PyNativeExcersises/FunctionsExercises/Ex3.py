"""
Exercise 3: Return multiple values from a function
Write a program to create function calculation()
such that it can accept two variables and calculate addition and subtraction.
 Also, it must return both addition and subtraction in a single return call.

Given:
"""


def calculation(a, b):
    res1 = a + b
    res2 = a - b
    return res1, res2

res = calculation(40, 10)
print(res)