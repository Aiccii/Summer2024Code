"""
Exercise 18: Print the following pattern
Write a program to print the following start pattern using the for loop

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

"""

# my solution
tracker = 0
ranger = 5

if tracker != 5 :
    for i in range(1, ranger + 1):
        for j in range(i):
            print("*", end=" ")
        print()

        tracker = tracker + 1

if tracker == 5:
    for i in range(ranger - 1, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()


# the official solution
print("\n\n")
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")