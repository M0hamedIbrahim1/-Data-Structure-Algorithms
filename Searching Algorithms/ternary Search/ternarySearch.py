def ternarySearch(arr,l,r,n):
    if l<=r:
        mid1 = l+(r-l) //3
        mid2 = r-(r-l) //3
        
        if arr[mid1] == n:
            return mid1
        if arr[mid2] == n:
            return mid2
        if n < arr[mid1]:
            return ternarySearch(arr,l,mid1-1,n)
        elif n > arr[mid2]:
            return ternarySearch(arr,mid2+1,r,n)
        else:
            return ternarySearch(arr,mid1+1,mid2-1,n)
    else:
        return -1
    
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
n = 13
A = ternarySearch(arr,0,len(arr)-1,n)
if A != -1 : 
    print("Element at index :", A)
else:
    print("Element is not in array")

  
  
  # output : Element at index : 12
  
