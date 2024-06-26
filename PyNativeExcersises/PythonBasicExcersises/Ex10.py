"""
Exercise 10: Create a new list from two list using the following condition
Create a new list from two list using the following condition

Given two list of numbers,
write a program to create a new list such that the new list should contain odd numbers
from the first list and even numbers from the second list.
"""

list11 = [10, 20, 25, 30, 35]
list22 = [40, 45, 60, 75, 90]


newList = []

def mergeList(list1, list2):
    for i in range(len(list1)):
        if list1[i] % 2 != 0:
            newList.append(list1[i])

    for i in range(len(list2)):
        if list2[i] % 2 == 0:
            newList.append(list2[i])



mergeList(list11, list22)

print(newList)