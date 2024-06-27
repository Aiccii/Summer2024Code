"""
Exercise 14: Reverse a given integer number
Given:

76542

Expected output:

24567

"""

num = 76542

numm = 0


print("initial number :",num )

while num > 0:
    rem = num % 10
    numm = (numm * 10) + rem
    num = num // 10

print(numm)