# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

new_string = "Hello, world"

def first_non_repeated_character(s):
    char_count = {}
    
    # Count the occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the first character with a count of 1
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None

result = first_non_repeated_character(new_string)
print(f"The first non-repeated character is: {result}")