# Find maximum profit for stocks in single transaction .

def profit_single(arr,n):
    max_profit = arr[1] - arr[0]
    minn = arr[0]
    for i in range (1,n):
        max_profit = max(max_profit,arr[i]-minn)
        minn = min(minn,arr[i]) 
    return max_profit

arr = list(map(int,input("enter the numbers : ").split(",")))
n = len(arr)
print(profit_single(arr,n))    



# find maximum profit for multiple transactions 

def profit_multiple(arr,n):
    profit = 0
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            profit += arr[i] - arr[i-1]
    return profit  

arr = list(map(int,input("enter the numbers : ").split(",")))
n = len(arr)
print(profit_multiple(arr,n))    



