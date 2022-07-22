def BinarySearch(lst,l,r,n):
    while r>=l:
        mid = (l+r)//2
        if arr[mid] == n:
            return mid
        elif n > arr[mid]:
            l = mid+1
        else:
            r = mid-1
    return -1

arr = [2,14,20,25,28,33,34,40,44,60]
n = 44
A = BinarySearch(arr,0,len(arr)-1,n)
if A != -1:
    print("Element at index :",A)
else:
    print("Element is not in array")

    
#output     
# Element at index : 8
