def BubbleSort(arr):
    l = len(arr)
    n = l-1
    while n >= 1:
        i = 0
        while i < n:
            if arr[i] > arr[i+1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i+=1
        n = n-1


arr = [5,2,9,13,8,20,15,18,23,7]
BubbleSort(arr)
print(arr)

# output : [2, 5, 7, 8, 9, 13, 15, 18, 20, 23]
# The worst and average-case time complexities of Bubble Sort are both O(n2)
