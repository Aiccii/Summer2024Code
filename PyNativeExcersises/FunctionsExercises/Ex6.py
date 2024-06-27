"""
Exercise 6: Create a recursive function
Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

A recursive function is a function that calls itself again and again.

Expected Output:

55

"""


def recursive(number):
    if number != 0:
        # this function keeps calling itself and subtracting 1 each time it does it
        return number + recursive(number - 1)
    else:
        return 0

inee = recursive(10)

print(inee)