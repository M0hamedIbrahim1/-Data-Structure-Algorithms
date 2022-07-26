 def exponentialSearch(arr,l,n):
        if arr[0] == n:
            return 0
        i = 1
        while i < l and arr[i] <= n:
            i*=2
        return binarysearch(arr,i//2,min(i,l-1),n)
def binarysearch(arr,l,r,n):
    if l <= r :
        mid = (l+r)//2
        if arr[mid] == n:
            return mid
        if arr[mid] < n:
            return binarysearch(arr,mid+1,r,n)
        if arr[mid] > n:
            return binarysearch(arr,l,mid-1,n)
    return -1
    
arr = [3,8,10,14,18,20,24,27,35]
n = 27
A = exponentialSearch(arr,len(arr),n)
if A != -1:
    print("Element found at index", A)
else:
    print("Element not found")
    
    
# output : Element found at index 7

