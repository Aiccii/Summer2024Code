"""
Exercise 1: Create a function in Python
Write a program to create a function that takes two arguments, name and age, and print their value.

"""

name = input("Enter a name : ")
age = int(input("Enter an age : "))



def name_and_age_function(name, age):
    print(f"\nName : {name}\nAge : {age}")

name_and_age_function(name, age)


# a prompt function
def prompto():
    name1 = input("\nEnter a name : ")
    age1 = int(input("Enter an age : "))
    print(f"\nName : {name1}\nAge : {age1}")

prompto()
