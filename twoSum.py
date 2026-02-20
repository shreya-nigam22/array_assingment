# Find Pair with Given Sum: Find a pair of elements that adds up to a target sum.

def twoSum(arr,n,sum):
    for i in range(n):
        if sum - arr[i] == arr[i]:
            continue
        if sum - arr[i] in arr:
            return (arr[i],sum-arr[i])
        
arr = list(map(int,input("enter the numbers : ").split(",")))   
n = len(arr)
sum = int(input("enter a num : "))
print(twoSum(arr,n,sum))         