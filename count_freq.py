# Count Frequency of Elements

def count_freq(arr,n):
    mydict = dict()
    for i in range(n):
        mydict[arr[i]] = 0
    for i in range(n):
        mydict[arr[i]] += 1
    for x in mydict:
        print(x," ",mydict[x])
    

arr = list(map(int,input("enter the numbers : ").split(",")))   
n = len(arr)
count_freq(arr,n)             

            