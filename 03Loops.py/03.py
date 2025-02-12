
# 3. Multiplication Table Printer
#  Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

num = int (input("Enter the number :"))
for i in range(num +1):
    print(num,"X",i,"=",num*i)