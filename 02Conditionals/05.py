# Weather Activity Suggestion
# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

activity = {
    "Sunny": "Go for a walk",
    "Rainy": "Read a book",
    "Snowy": "Build a snowman"
}

weather =  input("enter the weather :")
if weather == "Sunny":
    print(activity["Sunny"])
elif weather == "Rainy":
    print(activity["Rainy"])
elif weather == "Snowy":
    print(activity["Snowy"])