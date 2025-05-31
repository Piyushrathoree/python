
# 3. Multiplication Table Printer
#  Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

num = int(input("enter the number you want to have table of "))
for i in range(1, 11):
    if i == 5:
        continue
    print(num, "X", i, "=", num * i)