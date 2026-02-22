def profit_multiple(arr,n):
    profit = 0
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            profit += arr[i] - arr[i-1]
    return profit  


arr = list(map(int,input("enter the numbers : ").split(",")))
n = len(arr)
print(profit_multiple(arr,n))    

