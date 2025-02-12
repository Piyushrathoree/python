# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

def recommend_pet_food(species, age):
    if species == "dog":
        if age <= 2:
            print( "Puppy food")
        else:
            print("Regular dog food")
    elif species == "cat":
        if age >= 5:
            print ("Senior cat food")
        else:
            print ("Regular cat food")

# Test the function

species = input("Enter the pet's species: ")
age = int(input("Enter the pet's age: "))


recommend_pet_food(species, age)