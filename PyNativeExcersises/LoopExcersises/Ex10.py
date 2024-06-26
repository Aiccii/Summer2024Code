"""
Exercise 10: Use else block to display a message “Done” after successful execution of for loop
For example, the following loop will execute without any error.

Given:

for i in range(5):
    print(i)
Expected output:

0
1
2
3
4
Done!

"""

num = int(input("Enter a number to count to 0 : "))

for i in range(num + 1):
    print(i)
    print("Done!")


"""
# could be done like this too

for i in range(num + 1):
    print(i)
else:
    print("Done!")
"""