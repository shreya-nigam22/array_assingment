# Find the Maximum & Minimum Element

def max_min(arr,n):
    if n==0:
        return("no max")
    maximum = arr[0]
    minimum = arr[0]
    for i in range(1,n):
        if arr[i] > maximum:
            maximum = arr[i]
        elif arr[i] < minimum:
            minimum = arr[i]    
    return maximum , minimum

arr = list(map(int,input("enter the numbers : ").split(",")))   
n = len(arr)
print(max_min(arr,n))
