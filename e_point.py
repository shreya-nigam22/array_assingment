# Find Equilibrium Index: Find an index such that sum of elements on left = sum on right.


def e_point(arr,n):
    l_sum = 0
    r_sum = sum(arr)
    for i in range(n):
        r_sum -= arr[i]
        if l_sum == r_sum:
            return i
        l_sum += arr[i]
    return -1    

arr = list(map(int,input("numbers : ").split(",")))
n = len(arr)
print(e_point(arr,n))