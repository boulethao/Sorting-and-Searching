# IN PLACE MERGE SORT



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

    k = lo
    #modified insertion sort from mid+1 (left side is already sorted)
    for i in range(mid+1, hi+1):
        key = arr[i]

        j = i-1

        while j >= k and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

        k += 2




arr = [64, 34, 25, 12, 22, 1, 90]
mergesort(arr)

print(arr)


