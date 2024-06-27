"""
Exercise 15: Use a loop to display elements from a given list present at odd index positions
Given:

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Note: list index always starts at 0

Expected output:

20 40 60 80 100

"""


my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range( len(my_list)):
    if (i + 1) % 2 == 0:
        print(my_list[i], end=" ")

print("\n\nSecond Version")

# can be also done like this,
# Use list slicing. Using list slicing, we can access a range of elements from a list

for i in my_list[1::2]:
    print(i, end=" ")