def InsertionSort(array):
    i = 1
    while i < len(array):
        j = i
        while j:
            if array[j - 1] < array[j]:
                break
            array[j - 1], array[j] = array[j], array[j - 1]
            j = j - 1
        i = i + 1

array1 = [8, 9, 2, 5, 7, 1, 6, 4, 3, 0]
InsertionSort(array1)
print(array1)

#output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# The average and worst-case time complexity of the Insertion Sort is O(n2)
