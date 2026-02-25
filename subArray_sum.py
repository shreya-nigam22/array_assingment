# Find Subarray with Given Sum.

def sub_sum(arr,n,x):
    curr = 0
    s = 0
    for i in range(n):
        curr += arr[i]
        while curr > x:
            curr -= arr[s]
            s += 1
        if curr == x:
            return arr[s:i+1]    
    return -1

arr = list(map(int,input("enter the numbers : ").split(",")))   
n = len(arr)
x = int(input("enter any number : "))
print(sub_sum(arr,n,x))    
    