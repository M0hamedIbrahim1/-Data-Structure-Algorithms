 def interpolationSearch(arr,l,r,n):
        
        #array is sorted so the element must be in range l : r
        if l<=r and n >= arr[l] and n<= arr[r]:
            
            pos = l + ((r - l) // (arr[r] - arr[l]) * (n - arr[l]))            
            if arr[pos] == n:
                return pos
            
            # If n is larger, n is in right subarray
            if n > arr[pos]:
                return interpolationSearch(arr,pos+1,r,n)
            
            # If n is smaller, n is in left subarray
            if n < arr[pos]:
                return interpolationSearch(arr,l,pos-1,n)
            
        return -1

arr = [3,8,10,14,18,20,24,27,35]
n = 27
A = interpolationSearch(arr,0,len(arr)-1,n)
if A != -1:
    print("Element found at index", A)
else:
    print("Element not found")
    
    
 # output : Element found at index 7
