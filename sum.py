# Find the Sum of Elements

def sum_element(arr,n):
    sum = 0
    for i in range(0,n):
        sum+=arr[i]

    return sum 


arr = list(map(int,input("enter the numbers : ").split(",")))   
n = len(arr)
print(sum_element(arr,n))    
    