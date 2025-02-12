
# # 6. Factorial Calculator
#  Problem: Compute the factorial of a number using a while loop.

n = int(input("Enter a number: "))
factorial = 1
while n>0:
    factorial *= n
    n -= 1

print("Factorial is", factorial)
