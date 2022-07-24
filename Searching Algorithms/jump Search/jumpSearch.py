import math as m
def jumpSearch(arr,l,n):

    step = s = int(m.sqrt(l))
    current_step = 0
    
    # Finding the block where element is in.
    # (if it's in array)
    while arr[min(step,l)-1] < n:
        current_step = step
        step+=s
        if current_step >= l:
            return -1
    while arr[current_step] < n:
        current_step+=1
        
        if current_step == min(step,l):
            return -1

    if arr[current_step] == n:
        return current_step
    return -1
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
n = 13
l = len(arr)
A = jumpSearch(arr,l,n)
if A != -1 : 
    print("Element at index :", A)
else:
    print("Element is not in array")
    
# output : Element at index : 12
