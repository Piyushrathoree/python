#  8. Prime Number Checker
#  Problem: Check if a number is prime.

n = 49
is_prime= True
 
if n > 1:
    for i in range(2,n):
        if(n%i)==0:
            is_prime=False
            
if(is_prime):
    print("yes the given number is prime ")
else:
    print("no the given number is not prime ")
             