"""
Exercise 3: Calculate the sum of all numbers from 1 to a given number
Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

Expected Output:

Enter number 10
Sum is:  55

"""

num = int(input("Enter number : "))

sum = 0

for i in range(num + 1):
    sum = sum + i

print(f"Sum of all numbers {sum}")


# 2 solutions

# solution 1

# s: store sum of all numbers
s = 0
n = int(input("\n\nEnter number "))
# run loop n times
# stop: n+1 (because range never include stop number in result)
for i in range(1, n + 1, 1):
    # add current number to sum variable
    s += i
print("\n")
print("Sum is: ", s)



# solution 2 using the sum function
n = int(input("\n\nEnter number "))
# pass range of numbers to sum() function
x = sum(range(1, n + 1))
print('Sum is:', x)