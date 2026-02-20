# Find Union of Two Arrays

def union(arr1,arr2):
    s1 = set(arr1)
    res = list(s1)
    for i in arr2:
        if i not in s1:
            res.append(i)
    return res

arr1 = list(map(int,input("enter the numbers : ").split(",")))
arr2 = list(map(int,input("enter the numbers : ").split(",")))
print(union(arr1,arr2))     
