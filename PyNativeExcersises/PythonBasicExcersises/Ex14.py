"""
Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)

* * * * *
* * * *
* * *
* *
*

"""

for i in range(5,0, -1):
    for j in range(i):
        print("*", end=" ")

    print("")
