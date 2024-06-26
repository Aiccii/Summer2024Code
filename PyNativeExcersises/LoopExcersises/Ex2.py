"""
Exercise 2: Print the following pattern
Write a program to print the following number pattern using a loop.

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""

listo = []

for i in range(1,6):
    listo.append(i)
    for j in range(0, len(listo)):
        print(listo[j], end=" ")
    print()

# can be answered like this


print("\n\nNumber Pattern ")

# Decide the row count. (above pattern contains 5 rows)
row = 5
# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1
# run loop 5 times
for i in range(1, row + 1, 1):
    # Run inner loop i+1 times
    for j in range(1, i + 1):
        print(j, end=' ')
    # empty line after each row
    print("")