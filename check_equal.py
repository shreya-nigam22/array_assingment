# Check if Two Arrays Are Equal: if two arrays contain the same elements


def check_eq(arr1,arr2):
    if len(arr1) != len(arr2):
        return False
    s = set(arr1)
    for i in arr2:
        if i not in s:
            return False
    return True


arr1 = list(map(int,input("enter the numbers : ").split(",")))
arr2 = list(map(int,input("enter the numbers : ").split(",")))
print(check_eq(arr1,arr2))     
