# Find Intersection of Two Arrays: Find the common elements between two arrays.


# sorted arrays
def intersection(arr1,arr2,n,m):
    i = 0
    j = 0
    res = []
    while i<n and j<m:
        if arr1[i] == arr2[j]:
            res.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1    
        else:
            j += 1    
    return res

arr1 = list(map(int,input("enter the numbers : ").split(",")))
n = len(arr1)
arr2 = list(map(int,input("enter the numbers : ").split(",")))
m = len(arr2)
print(intersection(arr1,arr2,n,m))     



#unsorted arrays
def intersection(arr1,arr2):
    s = set(arr1)
    res = []
    for i in arr2:
        if i in s:
            res.append(i)
            s.remove(i)
    return res

arr1 = list(map(int,input("enter the numbers : ").split(",")))
arr2 = list(map(int,input("enter the numbers : ").split(",")))
print(intersection(arr1,arr2))     



