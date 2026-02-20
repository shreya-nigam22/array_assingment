# Reverse an array

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

arr = list(map(int,input("enter the numbers : ").split()))
print(reverse(arr))    