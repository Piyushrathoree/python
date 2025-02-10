# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

marks={
    "rohan":60,
    "rahul":78,
    "priya":92
}

name = input("What is your name ?")

if marks[name] >= 90 :
    print("your marks are :",marks[name])
    print("your grade is : A" )
elif marks[name] >= 80 and marks[name] < 90:
    print("your marks are :",marks[name])
    print("your grade is : B" )
elif marks[name] >= 70 and marks[name] < 80:
    print("your marks are :",marks[name])
    print("your grade is : c" )
elif marks[name] >= 60 and marks[name] < 70:
    print("your marks are :",marks[name])
    print("your grade is : D" )
else:
    print("your marks are :",marks[name])
    print("your grade is : E \n very bad you need to study" )

