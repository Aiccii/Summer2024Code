"""
Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
Note here exp is a non-negative integer, and the base is an integer.
"""

def exponent(base, exp):
    val = 1
    for i in range(exp):
        val = val * base

    print(f"{base} raised to the power {exp} : {val}")


exponent(5,4)