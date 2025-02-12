#  Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
items = ["apple", "banana", "orange", "apple", "mango","mango"]
duplicates = []
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i] == items[j]:
            duplicates.append(items[i])
    

print(duplicates)