# find the maximum sum in circular array

def normal_sum(arr,n):
    max_ending = arr[0]
    res = arr[0]
    for i in range(1,n):
        max_ending = max(max_ending + arr[i],arr[i])
        res = max(res,max_ending)
    return res

def overall_sum(arr,n):
    max_normal = normal_sum(arr,n)
    if max_normal < 0:
        return max_normal
    arr_sum = 0
    for i in range(n):
        arr_sum += arr_sum
        arr[i] = -arr[i]
    max_circular = arr_sum - normal_sum(arr,n)
    maxx = max(max_normal,max_circular)  
    return maxx      


arr = list(map(int,input("enter the numbers : ").split(",")))
n = len(arr)
print(overall_sum(arr,n))