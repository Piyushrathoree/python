# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

new_string = "python is decent but python is easy"

for char in new_string:
   if new_string.count(char) ==1: # this method helps in checking the count of a specific character 
       print(char)
       break        
