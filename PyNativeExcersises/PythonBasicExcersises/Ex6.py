"""
Exercise 6: Display numbers divisible by 5 from a list

Iterate the given list of numbers and print only those numbers which are divisible by 5

Given list is  [10, 20, 33, 46, 55]
Divisible by 5
10
20
55

"""

listItem = [10, 20, 33, 46, 55]

for i in range(len(listItem)):
    if listItem[i] % 5 == 0:
        print(listItem[i])

