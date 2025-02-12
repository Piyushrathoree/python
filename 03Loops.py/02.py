# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
sum=0
for num in numbers:
    if num%2==0:
        sum = sum+num
        
print(sum)
