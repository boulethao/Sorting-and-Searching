# SELECTION SORT

# Selection sort find the smallest element by scanning from beginning towards the end of the array and swap it
# with the first index of the array. Repeat with the second element in the array, and so on, until completed sorted.

# Time complexity:
#   Best: O(n^2)
#   Average: O(n^2)
#   Worst: O(n^2)

# Space complexity: O(1)

# Stable? No

# N.B. Not the best choice of sorting (runtime always quadratic).
# But selection sort doesn't make more than O(n) swaps. Useful when memory write is a constraint.



def selectionsort(arr):
    if arr is None or len(arr) <= 1:
        return arr

    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


# Run selection sort
arr = [64, 34, 25, 12, 22, 1, 90]
selectionsort(arr)
print(arr)