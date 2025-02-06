n=int(input("Enter the number:"))
def printConsecutiveNum(n):
    output= []
    for i in range(0,n+1):
        if(i<n+1):
            output.append(i)
    str_list = [str(num) for num in output]
    combined_str = "".join(str_list)
    result = int(combined_str)
    return result
    
print(printConsecutiveNum(n))  
