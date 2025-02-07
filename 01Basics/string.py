chai = "Lemon Chai"
anotherChai = "normal"
print(chai.lower())
print(chai.upper())
print(chai.strip())
print(chai.replace("Lemon", "Ginger"))
print(chai.split(" "))
print(chai.find("Chai"))  # [returns -1 if it doesn't exist]
print(chai.count("Chai"))
print(",".join(anotherChai))
print(len(chai))
print(r"Masala\nchai")  # [mainly used in paths (avoid backslash at last)]
print("Masala" in chai)
#print(chai.append(anotherChai))  # [not a valid operation in Python]))
print(chai.index("Chai"))  # [returns ValueError if it doesn't exist]   
print(chai + " "+ anotherChai)