# Merge Two Sorted Arrays

def merge(arr1,arr2):
    n = len(arr1)
    m = len(arr2)
    i = 0
    j = 0
    res = []
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1  
    res.extend(arr1[i:])
    res.extend(arr2[j:])
    return res    

arr1 = list(map(int,input("enter the numbers : ").split(",")))
arr2 = list(map(int,input("enter the numbers : ").split(",")))
print(merge(arr1,arr2))

            