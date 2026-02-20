# Remove given Element from Array


def remove(arr,n,x):
    res = []
    for i in range(n):
        if arr[i] != x:
            res.append(arr[i])
    return res

arr = list(map(int,input("enter the numbers : ").split(",")))  
n = len(arr)
x = int(input("enter a number you want to remove from the array : "))    
print(remove(arr,n,x))  

