print("hello world")

def test(x):
    print("Running tests...")

test(5)   

# all about the storaging of data in python 

    # primitive data types: int, float, bool, str

    # compound data types: list, tuple, dict, set

    # mutable and immutable: lists, tuples, sets are mutable, while ints, floats, bools, strs are immutable
    
    # variable scope: variables defined inside a function are local to that function, unless explicitly declared global
    
    # variable naming conventions: snake_case for variables, UPPER_CASE for constants, start with a letter or underscore

    # data type conversion: int(x), float(x), str(x), bool(x)

    # type checking: type(x)

# whenever we are assigning a value to immutable data type, a new object is created in memory, and the original object is not modified which is stored in memory. if you assign it another vairable then it will build an another object and take its reference and after some time the old one get deleted by garbage collector .

# example:
a=5 
b=a
a = 10 
print(a , b) # here the value of a and b will be 10 and 5 becuase b is holding the old reference of a 

# whenever we are assigning a value to mutable data type, the original object will be modified in memory.whenever user perform any operatation , but if any other value is having the refernce with the original object then it will be affected , because it is a mutable data type.

# example:

c = [1,2,3]
d = c
c[0] = 10
print(c , d) # here the value of c and d will be [10,2,3] and [10,2,3] becuase d is holding the old reference of c , and the changes are performed in the memory on original object.

# but if i make a copy of mutable data type using slicing then it will not affect the original object.

e = c[:]
e[1] = 5
print(c , e) # here the value of c and e will be [10,2,3] and [10,5,3] but both are different and now if i made changes in one then the other will not be affected.

# is operator checks if two variables refer to the same object in memory.
m = [1 ,2, 3]
n = m 
print(m==n )
print(m is n)

n=[1,2,3] # looking same as old but different object in memory
print(m == n)
print(m is n )

