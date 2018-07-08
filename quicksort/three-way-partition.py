# 3-ways partition



def three_ways_partition(arr):
    if arr is None or len(arr) <= 1:
        return



    low = 0
    high = len(arr)-1
    i = 0

    pivot = arr[i]

    while i <= high:

        if arr[i] < pivot:
            arr[i], arr[low] = arr[low], arr[i]

            low += 1
            i += 1

        elif arr[i] == pivot:
            i += 1

        elif arr[i] > pivot:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1


arr = ["7", "10", "8", "7", "2", "9", "0", "7", "8", "10", "11", "9", "7", "3", "8", "3"]
three_ways_partition(arr)
print (arr)