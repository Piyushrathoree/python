chai_types = {'masala':'spicy' , "ginger": "zesty" , "green":"mild"}

# print all keys in the dictionary
print(chai_types)

# print all values in the dictionary

for value in chai_types.values():
    print(value)

for chai in chai_types:
    print(chai, chai_types[chai])

# we can also use two different variable in loop 
for key, value in chai_types.items():
    print(key, value)

if 'masala' in chai_types:
    print("Masala is in the dictionary")

len_chai_types = len(chai_types)
print("Length of the dictionary is", len_chai_types)

#addding new key-value pair
chai_types['elaichi'] = 'sweet'
print(chai_types)

# deleting a key-value pair

del chai_types['elaichi']  # delete totally from memory reference
print(chai_types)
#or 
chai_types.pop('ginger')
print(chai_types)


# updating a value

chai_types['masala'] = 'spicy'
print(chai_types)


chai_copy = chai_types.copy()

# check if two dictionaries are equal

print(chai_types == chai_copy)
print(chai_types is chai_copy)


tea_shop = {"chai":{"price":10, "quantity":50}, "green tea":{"price":5, "quantity":100}}
print(tea_shop)

print(tea_shop["chai"]["price"])

# creating new dict from list 
pen = ["blue", "black", "green"]
price="good"

pen_dict = dict.fromkeys(pen, price)

print(pen_dict)

