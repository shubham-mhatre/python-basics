
##print square of all numbers between 1 and 10 except for even numbers

for items in range(1, 10):
    if items % 2 == 0:
        continue
    print(items * items)
