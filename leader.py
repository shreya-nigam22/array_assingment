# Find the Leader Elements: An element is a leader if it is greater than all elements to its right.

def leader(arr,n):
    maxx = arr[-1]
    res = [maxx]
    for i in range(n-2,-1,-1):
        if arr[i] > maxx:
            maxx = arr[i]
            res.append(arr[i])
    return res[::-1]

arr = list(map(int,input("enter a numebrs : ").split(",")))
n = len(arr)    
print(leader(arr,n))    