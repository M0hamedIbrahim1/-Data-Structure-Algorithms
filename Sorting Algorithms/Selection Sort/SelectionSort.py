def SelectionSort(arr):
    i = 0
    while i < len(arr):
        j = i
        k = j + 1
        while k < len(arr):
            if arr[k] < arr[j]:
                j = k
            k+=1
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        
arr = [5,2,9,13,8,20,15,18,23,7]
SelectionSort(arr)
print(arr)

# output : [2, 5, 7, 8, 9, 13, 15, 18, 20, 23]
