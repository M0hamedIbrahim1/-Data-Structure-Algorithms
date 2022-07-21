def LinearSearch(lst,n,x):
    for i in range(n):
        if lst[i] == x:
            return i
    return -1
    
    
lst = [210,197,125,324,185,240,380,140]
x = 185
n = len(lst)
A = LinearSearch(lst,n,x)


if A != -1:
    print("Found , in index : ", A)
else: print("Not Found")
  
