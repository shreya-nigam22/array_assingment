# Maximum Sum Subarray (Kadane's Algorithm)

def max_sum(arr,n):
    max_ending = arr[0]
    res = arr[0]
    for i in range(1,n):
        max_ending = max(max_ending + arr[i],arr[i])
        res = max(res,max_ending)
    return res

arr = list(map(int,input("enter the numbers : ").split(",")))
n = len(arr)
print(max_sum(arr,n))    
