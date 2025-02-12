# 4. Reverse a String
# Problem: Reverse a string using a loop.

def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

# Example usage
input_string = "Hello, World!"
print(reverse_string(input_string))



    
