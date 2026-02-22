# Find the maximum difference 

def max_diff(arr,n):
    res = arr[1] - arr[0]
    minn = arr[0]
    for i in range(1,n):
        res = max(res,arr[i]-minn)
        minn = min(minn,arr[i])
    return res

arr = list(map(int,input("enter the numbers : ").split(",")))
n = len(arr)
print(max_diff(arr,n))    
