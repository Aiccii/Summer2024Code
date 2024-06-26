"""
Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
Use the print() function to format the given words in the mentioned format.
Display the ** separator between each string.

Expected Output:

For example: print('Name', 'Is', 'James') will display Name**Is**James

"""


def printFunction(name):
    name2 = str(name).split(' ')
    for i in range(len(name2)):
        print(name2[i],end="**")
    print("\b\b")

printFunction("My Name Is James")

# another way that is less flexible but still works
print('My', 'Name', 'Is', 'James', sep='**')
