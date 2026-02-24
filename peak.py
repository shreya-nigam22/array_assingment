# Find Peak Element: A peak element is greater than its neighbors. Find one such element.


def peak(arr,n):
    i = 0
    j = n-1
    while i<=j:
        mid = (i+j)//2
        if (mid == 0 or arr[mid] > arr[mid-1]) and (mid == n-1 or arr[mid] > arr[mid+1]):
            return mid
        elif arr[mid] < arr[mid-1]:
            j = mid-1
        else:
            i = mid+1

arr = list(map(int,input("enter the numbers : ").split(",")))            
n = len(arr)
print(peak(arr,n))     
