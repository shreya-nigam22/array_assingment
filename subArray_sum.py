# Find Subarray with Given Sum.

def sub_sum(arr,n,x):
    prefix_map = {}
    curr_sum = 0
    for i in range(n):
        curr_sum += arr[i]
        if curr_sum == x:
            return 0, i
        if (curr_sum - x) in prefix_map:
            return prefix_map[curr_sum - x] + 1, i
        prefix_map[curr_sum] = i
    return -1


arr = list(map(int,input("enter the numbers : ").split(",")))   
n = len(arr)
x = int(input("enter any number : "))
print(sub_sum(arr,n,x))    
    