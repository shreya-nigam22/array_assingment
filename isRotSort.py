

def isRotatedSorted(arr,n):
    count = 0
    for i in range(n):
        if arr[i] > arr[(i+1) % n]:
            count += 1
    if count == 1:
        return True
    return False



arr = list(map(int,input("enter numbers : ").split(",")))
n = len(arr)
print(isRotatedSorted(arr,n))