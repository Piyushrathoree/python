#1. Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

age = int (input("Enter your Age :"))
if age < 13 : 
    print("you're a child ")
elif age >= 13 and age < 19:
    print("you're a teenager right now ")
elif age >=19 and age <= 59 :
    print("you're an adult")
elif age >59 :
    print("you're a senior citizen")

