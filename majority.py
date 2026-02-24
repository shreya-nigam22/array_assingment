# Find the majority element

def majority(arr,n):
    count = 1
    res = arr[0]
    for i in range(1,n):
        if arr[i] == arr[i-1]:
            count += 1
        else:
            count -= 1

        if count == 0:
            res = i
            count = 1   
    count = 0
    for i in range(n):
        if arr[res] == arr[i]:
            count += 1
    if count > n//2:
        return arr[res]
    return -1   


arr = list(map(int,input("enter the numbers : ").split(","))) 
n = len(arr)
print(majority(arr,n))    
