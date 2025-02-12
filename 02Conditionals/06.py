# 6. Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

vehicles = ["Walk" , "Bike" , "Car"]
distance = int(input("how much distance are you going to travel?"))
if distance <= 3:
    print(vehicles[0])
elif distance <=15 and distance>3:
    print(vehicles[1])
else:
     print(vehicles[2])