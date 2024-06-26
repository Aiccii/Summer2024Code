"""
Exercise 9: Check Palindrome Number
Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

"""




def check_palindrome(number):
    print(f"Original number : {number}")
    original_number = number

    reverse = 0

    while number > 0 :
        remainder = number % 10
        reverse = (reverse * 10) + remainder
        number = number // 10


    if original_number == reverse :
        print("number is a palindrome")

    else :
        print("number is not a palindrome")



check_palindrome(212)