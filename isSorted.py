# Check if Array is Sorted

def isSorted(arr,n):
    inc = True
    dec = True
    i=0
    for i in range(1,n):
        if arr[i-1] > arr[i]:
            inc = False
        if arr[i-1] < arr[i]:
            dec = False
    if inc == True or dec == True :
        return 1 
    else:
        return 0
    
arr = list(map(int,input("enter the numbers : ").split(",")))   
n = len(arr)
print(isSorted(arr,n))    
                

