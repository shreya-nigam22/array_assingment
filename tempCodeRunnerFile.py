def moveAllZeroes(arr,n):
    j = 0
    for i in range(n):
        if arr[i] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            j += 1
    return arr

arr = list(map(int,input("enter the numbers : ").split(",")))
n = len(arr) 
print(moveAllZeroes(arr,n))