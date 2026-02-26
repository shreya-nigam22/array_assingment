# Find All Subarrays

def subarrays(arr,n):
    for i in range(n):
        for j in range(i,n):
            print(arr[i:j+1])

arr = list(map(int,input("enter the numbers : ").split(",")))
n = len(arr)
subarrays(arr,n)        
