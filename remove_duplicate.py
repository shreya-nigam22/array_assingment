# Remove Duplicates from Array: Remove duplicates from the array while maintaining order.

def removeDuplicate(arr):
    s=set(arr)
    return list(s) 

arr = list(map(int,input("enter the numbers : ").split(",")))
print(removeDuplicate(arr))