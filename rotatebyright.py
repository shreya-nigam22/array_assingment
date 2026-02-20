# Rotate Array by k Positions: Rotate the array to the right by k positions.


def reverse(arr):
    n=len(arr)
    if n<1:
        return arr
    i=0
    j=n-1
    while i<j:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1
    return arr

def rotate_Right(arr,n,k):
    arr[n-k:n] = reverse(arr[n-k:n])
    arr[0:n-k] = reverse(arr[0:n-k])
    arr[0:n] = reverse(arr[0:n])
    return arr

arr = list(map(int,input("enter the numbers : ").split()))
n=len(arr)
k=int(input("enter the number by which you want to rotate the array : "))
print(rotate_Right(arr,n,k))    