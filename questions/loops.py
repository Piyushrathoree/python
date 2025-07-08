import math
n = input("Enter a number: ")

for i in range (0,n):
    if(i<n):
        ans = int(math.pow(i,2))
        print(ans)
