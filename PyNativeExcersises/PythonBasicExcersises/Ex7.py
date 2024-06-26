"""
Exercise 7: Return the count of a given substring from a string
Write a program to find how many times substring “Emma” appears in the given string.
"""

str_x = "Emma is good developer. Emma is a writer"

# use the count function to know how many times something appears in the string
val = str_x.count("Emma")

print(f"Emma appears {val} times")