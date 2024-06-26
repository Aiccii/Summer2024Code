"""
Exercise 7: Print the following pattern
Write a program to use for loop to print the following reverse number pattern

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

"""

num = 5


for i in range(5, 0, -1):

    newNum = num
    for j in range(newNum, 0, -1):
        print(newNum, end=" ")
        newNum = newNum - 1

    print()
    num = num - 1