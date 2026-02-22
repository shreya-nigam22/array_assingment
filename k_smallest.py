# Find the Kth Smallest Element

def k_smallest(arr,n,k):
    if k>n:
        return False
    arr.sort()
    return(arr[k-1])

arr = list(map(int,input("enter the numbers : ").split(",")))
n = len(arr)
k = int(input("enter any number : "))
print(k_smallest(arr,n,k))
