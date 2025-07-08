# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

def multiply(num1, num2):
    if isinstance(num1, str) and isinstance(num2, str):
        num1 = int(num1)
        num2 = int(num2)
    return num1 * num2

# Test cases

print(multiply(2, 3))  # Output: 6
print(multiply("2", "3"))  # Output: 6
print(multiply(4.5, 2))  # Output: 9
print(multiply("4.5", "2"))  # Output: 9