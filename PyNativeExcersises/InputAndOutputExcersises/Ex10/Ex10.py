"""
Exercise 10: Read line number 4 from the following file

Create a test.txt file and add the below content to it.

test.txt file:

line1
line2
line3
line4
line5
line6
line7

"""

fp = open('test.txt', 'r')

print(fp.readlines()[3])
