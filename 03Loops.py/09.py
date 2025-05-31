#  Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

fruits = ['apple','banana','mango','pineapple','grapes']

for fruit in fruits:
    if fruits.count(fruit) > 1:
        print(fruit)
        break
    
print("every fruit in the basket is unique")