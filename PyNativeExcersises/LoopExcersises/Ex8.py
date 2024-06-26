"""
Exercise 8: Print list in reverse order using a loop
Given:

list1 = [10, 20, 30, 40, 50]
Expected output:

50
40
30
20
10

"""

list1 = [10, 20, 30, 40, 50]

print("Version 1")
for i in range(len(list1) - 1 , - 1, -1):
    print(list1[i])


# you could reverse the whole damn list

print("\n\nVersion 2")
newlist = reversed(list1)

for new in newlist:
    print(new)