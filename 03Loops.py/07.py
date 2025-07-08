
# # 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.


while True:
    number = int(input("enter the number :"))
    if 1<=number<=10:
        print('you have enter the value in the right range ')
        break