# Find the minimum number of consecutive flips to make a binary araay same 

def min_flips(arr,n):
    for i in range(1,n):
        if arr[i-1] != arr[i]:
            if arr[i] != arr[0]:
                print("from",i,"to",end=" ")
            else:
                print(i-1)
    if arr[n-1] != arr[0]:
        print(n-1)

arr = list(map(int,input("enter the numbers : ").split(",")))
n = len(arr)
min_flips(arr,n)
        