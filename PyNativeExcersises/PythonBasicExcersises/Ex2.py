"""
Exercise 2: Print the sum of the current number and the previous number

Write a program to iterate the first 10 numbers, and in each iteration,
print the sum of the current and previous number.

"""

for i in range(1, 11):
    prev = i - 1
    sum = prev + i
    print(f"Current Number {i}, Previous Number {prev}, the Sum {sum}")