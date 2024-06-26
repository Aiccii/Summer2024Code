"""
Exercise 6: Count the total number of digits in a number
Write a program to count the total number of digits in a number using a while loop.

For example, the number is 75869, so the output should be 5.

"""

inpp = str(input("Enter a number to count the number of digits : "))

cnt = 0
for i in range(len(inpp)):
    cnt = cnt + 1

print("the amount of digits is :", cnt)


# the answer that can be different

num = 758693
count = 0
while num != 0:
    # floor division
    # to reduce the last digit from number
    num = num // 10

    # increment counter by 1
    count = count + 1
print("Total digits are:", count)