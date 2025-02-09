#tuple method 

    # Define a tuple
my_tuple = ("apple", "banana", "cherry")

    # Accessing elements using index
print(my_tuple[0])

# Slicing a tuple

print(my_tuple[1:3])

# Changing elements in a tuple is not possible

# Tuples are immutable, meaning they cannot be changed after they are created. If you want to modify an element in a tuple, you have to convert it to a list, modify the list, and then convert it back to a tuple.
# all the mothod are same as list but we can't manipulate tuple like list because it is immutable 

# Unpacking a tuple # same scene are destructuring  in js 
mytuple2 = ("fruits" , "vegetables")
(fruits, vegetables) = mytuple2
print(fruits)
print(vegetables)

# Deleting a tuple

del my_tuple

print(mytuple2) 
# this will give error because tuple is deleted

