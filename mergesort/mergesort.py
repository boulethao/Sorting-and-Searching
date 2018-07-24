# MERGE SORT

# Merge sort is a divide-and-conquer algorithm. It divides the array in half repetitively until those halves have only
# one item. The it merge back these halves by insuring that the elements are sorted.

# Time complexity:
#   best: O(n log n)
#   average: O(n log n)
#   worst: O(n log n)

# Space complexity: O(n) for arrays / O(n log n) for linked lists

# Stable? Yes

def mergesort(arr):
    if arr is None or len(arr) <= 1:
        return arr

    _mergesort(arr, 0, len(arr)-1)

def _mergesort(arr, lo, hi):
    if lo >= hi:
        return

    mid = (lo + hi) // 2

    _mergesort(arr, lo, mid)
    _mergesort(arr, mid+1, hi)

    merge(arr, lo, mid, hi)

def merge(arr, lo, mid, hi):

    left = arr[lo : mid+1]
    print(left)
    right = arr[mid+1 :  hi+1]

    i = 0
    j = 0

    k = lo

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


arr = [64, 34, 25, 12, 22, 1, 90]
mergesort(arr)

print(arr)


