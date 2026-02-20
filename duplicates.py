# Find Duplicates in an Array

def duplicate(arr,n):
    d = dict()
    for i in range(n):
        d[arr[i]] = 0
    for i in range(n):
        d[arr[i]] += 1
    l = []    
    for x in d:
        if d[x] != 1:
            l.append(x)   
    return l

arr = list(map(int,input("enter the numbers : ").split(",")))   
n = len(arr)
print(duplicate(arr,n))    
                            