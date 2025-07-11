import math
n = input("Enter a number: ")

for i in range (0,n):
    if(i<n):
        ans = int(math.pow(i,2))
        print(ans)

nums = [1,2,3,4]
for i in nums:
    print(nums[i])