"""
Exercise 5: Check if the first and last number of a list is the same

Write a function to return True if the first and last number of a given list is same.
If numbers are different then return False.

"""


def func(list):

    if list[0] == list[len(list)-1] :
        return print(True)

    else: return print(False)


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]


func(numbers_x)

print("second")
func(numbers_y)