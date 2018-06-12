# INSERTION SORT

# Iterate from the beginning of the array
# At each index, check if the key at that index is smaller than the ones on its left.
# Shift all these left elements to the right.
# Every shift to the right will create a "hole" at the original index.
# When there are no bigger elements left, insert the key into the hole.


def insertionsort(arr):
    """
    Insertion sort an array of integers
    :param arr (list): Array of integers
    :return:
    """

    if arr is None or len(arr) <= 1:
        return arr

    n = len(arr)

    # Iterate from index 1
    for i in range(1, n):
        # Key element to insert at the appropriate position on its left
        key = arr[i]

        # Check the first element on the left
        j = i-1

        # Shift the left element on the right and continue until left element is no longer bigger than key element
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        # Insert the key element on the "hole". This key is now placed at the right position.
        arr[j+1] = key


# Run insertion sort
arr = [64, 34, 25, 12, 22, 1, 90]
insertionsort(arr)
print(arr)