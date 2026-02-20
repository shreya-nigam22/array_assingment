# Find the Second Largest Element

def second_largest(arr,n):
    lar = arr[0]
    s_lar = None
    if n<1:
        return s_lar
    for i in range(1,n):
        if arr[i] > lar:
            s_lar = lar
            lar = arr[i]      
        else:
            if s_lar == None or arr[i] > s_lar :
                s_lar = arr[i] 

    return s_lar  

arr = list(map(int,input("enter the numbers : ").split(",")))   
n = len(arr)
print(second_largest(arr,n))         