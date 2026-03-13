# Print the row given the row number

def generate(n):
    ans = 1
    res = []
    for i in range(1,n+1):
        res.append(ans)
        ans = ans * (n-i)
        ans = ans // i
    return res

    
n = int(input("enter any number : "))
print(generate(n))



# Print the pascal's triangle upto the given row:


def triangle(n):
    res = []
    for i in range(n):
        ans = 1
        temp = []
        for j in range(i+1):
            temp.append(ans)
            ans = ans * (i-j)
            ans = ans // (j+1)
        res.append(temp) 
    return res



n = int(input("enter a number : "))
print(triangle(n))