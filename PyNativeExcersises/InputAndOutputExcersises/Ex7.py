"""
Exercise 7: Accept any three string from one input() call
Write a program to take three names as input from a user in the single input() function call.

See: Get multiple inputs from a user in one line

Enter three string Emma Jessa Kelly
Name1: Emma
Name2: Jessa
Name3: Kelly

"""

names = []

for i in range(1, 4):
    names.append(input(f"Enter Name {i} : "))

print("\n")

for i in range(1, len(names) + 1):
    print(f"Name {i} : " + names[i - 1])

# could be also done like this but my way is maintainable better

str1, str2, str3 = input("Enter Names seperated by a space : ").split()

print(f"Name 1 : {str1}")
print(f"Name 2 : {str2}")
print(f"Name 3 : {str3}")
