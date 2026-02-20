# Find the Missing Number: Find the missing number in an array of size n containing numbers from 1 to n.

def missing_num(arr,n):
    total_sum = m*(m+1)//2
    arr_sum = 0
    for i in range(n):
        arr_sum += arr[i]
    missing = total_sum - arr_sum
    return missing

arr = list(map(int,input("enter the numbers : ").split(",")))
n=len(arr)
m = int(input("enter the value of m : "))
print(missing_num(arr,n))
