def chooseDish(arr):
    d = {}
    for i in arr:
        d[i] = 1
    for i in arr:
        d[i] += 1
    max_count = 0
    res = None
    for c in d:
        count = (d[c]+1) // 2
        if count > max_count or (count == max_count and (res == None or c < res)):
            max_count = count
            res = c
    return res        

arr = list(map(int,input("enter any numbers : " ).split(",")))
print(chooseDish(arr))
