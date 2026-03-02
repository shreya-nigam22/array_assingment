# Find the index of the numbers in increasing order which sums to the target given


def twoSum(arr,n,x):
    if n < 0:
        return None
    d = {}
    for i in range(n):
        need = x - arr[i]
        if need in d:
            return [d[need],i]
        else:
            d[arr[i]] = i


arr = list(map(int,input("enter the numbers : ").split(",")))
n = len(arr)
x = int(input("enter the targeted sum : "))
print(twoSum(arr,n,x))
