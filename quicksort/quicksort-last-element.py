###
# QUICKSORT : LAST ELEMENT AS PIVOT
###

def quicksort_last(arr):
    """
    Quicksort by choosing the last element in the array as a pivot

    :param arr: array of integers to sort

    :return:
    """

    # Nothing to sort since we have only one element (or none)
    if arr is None or len(arr) <= 1:
        return

    _quicksort_last(arr, 0, len(arr)-1)

def _quicksort_last(arr, lo, hi):
    """
    This method is recursively called after partitioning the array.

    The partition method chooses a pivot (last element) and divides the array into two sub-arrays.
    The left one has elements which are smaller than the pivot and the right one has elements which are bigger than the
    pivot.
    After the partition, the pivot is placed at its right position in the array.

    Recursively calls this method on the left array and on the right array.

    :param arr: array of integers to sort
    :param lo: lower bound of the array
    :param hi: higher bound of the array

    :return:
    """
    if lo >= hi:
        return

    # Find the position of the pivot
    p = partition_last_element(arr, lo, hi)

    # Recursively call this method on the left partition and on the right partition (without the pivot)
    _quicksort_last(arr, lo, p-1)
    _quicksort_last(arr, p+1, hi)


def partition_last_element(arr, lo, hi):
    """
    Partition the array by choosing the last element as a pivot.

    :param arr: The array of integers to partition
    :param lo: The lower boundary of the array
    :param hi: The higher boundary of the array

    :return:
    """

    pivot = arr[hi]

    index = lo  # index cursor that walks through the array and compare all elements with the pivot
    p = lo - 1  # boundary position for all elements that are smaller than the pivot

    while index < hi:
        if arr[index] < pivot:
            # increase the boundary so we can set the element within the boundary
            p += 1
            arr[index], arr[p] = arr[p], arr[index]

        index += 1

    #when done, place the pivot right after the boundary of "< pivot"
    p += 1
    arr[hi], arr[p] = arr[p], arr[hi]

    # return the final position of the pivot
    return p



arr = [5, 2, 6, 1, 3, 4]
print("Quicksort %s with last element as a pivot" % arr)
quicksort_last(arr)
print("=> %s" % arr)

