"""
Exercise 5: Accept a list of 5 float numbers as an input from the user
Refer:

Take list as a input in Python.
Python list
Expected Output:

[78.6, 78.6, 85.3, 1.2, 3.5]

"""
listo = []
for i in range(5):
    listo.append(float(input("enter number : ")))

print(listo)