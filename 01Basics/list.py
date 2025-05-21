tea = ["black", "green", "oolong"];

print(tea)
print(tea[0])
print(tea[-1])# prints the last element of the list
print(tea[1:2])
# print(tea[1:2])= "lemon" # not possible
tea[1:2] =["lemon"]
print(tea)

for i in tea:
    print(i)
    
# append() method adds an element to the end of the list

tea.append("white")
print(tea)

# extend() method adds elements from another list to the end of the current list

more_tea = ["oolong", "herbal"]
tea.extend(more_tea)
print(tea)

# insert() method inserts an element at a specific index

tea.insert(2, "puerh")
print(tea)

# # remove() method removes the first occurrence of an element

# tea.remove("black")
# print(tea)

# pop() method removes the last element from the list

tea.pop()
print(tea)



# index() method returns the index of the first occurrence of an element

print(tea.index("black"))

# count() method returns the number of occurrences of an element

print(tea.count("black"))

# sort() method sorts the elements of the list in ascending order

tea = ["black", "green", "oolong", "white", "puerh", "herbal"]
tea.sort()
print(tea)

# reverse() method reverses the elements of the list

tea.reverse()
print(tea)

# copy() method returns a shallow copy of the list

new_tea = tea.copy()
print(new_tea)

# join() method concatenates all the elements of the list into a string

concatenated_tea = ", ".join(tea)
print(concatenated_tea)

# len() method returns the number of elements in the list

print(len(tea))

#performing operations in a new lists
squareNum = [i**2 for i in range(1,11)]

print(squareNum)

# clear() method removes all elements from the list

tea.clear()
print(tea)


# slicing any array will create its copy in the memory it will not point to the same reference
h1 = [1,2,3,4]
h2=h1[:]
h1[0]=22
print(h1 ,h2) # now the h2 is not pointing to the reference value of h1 it has it's own new object in the memory