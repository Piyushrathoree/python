
# # 6. Factorial Calculator
#  Problem: Compute the factorial of a number using a while loop.

number = int(input("enter the number :"))
factorial =1 
while number > 0:
    factorial *=number
    number -= 1

print(factorial)                