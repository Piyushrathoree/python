# Enter your code here. Read input from STDIN. Print output to STDOUTbgh
def check(line):
    start = line.index("#")
    end = line.index(";")
    print(line[start:end])
    
    
n = int(input())
code = []
for i in range(n):
    line=input().split()
    if len(line)>0:
        for k in range(len(line)):
            
            if "#" in line[k] and ";" in line[k]:
                check(line[k])
                code.append(line[k])
   



#preety complex logic for handling multiple comments and here the time complexity is broken 
