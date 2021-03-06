
###
# QUICKSORT : FIRST ELEMENT AS PIVOT
###
def quicksort_first(arr):
    """
    Quicksort by choosing the first element in the array as a pivot

    :param arr: array of integers to sort

    :return:
    """
    if arr is None or len(arr) <= 1:
        return

    _quicksort_first(arr, 0, len(arr)-1)


def _quicksort_first(arr, lo, hi):
    """
    This method is recursively called after partitioning the array.

    The partition method chooses a pivot (first element) and divides the array into two sub-arrays.
    The left one has elements whic are smaller than the pivot and the right one has elements which are bigger than the
    pivot.
    After the partition, the pivot is placed at its right position in the array.

    Recursively calls this method on the left array and on the right array.

    :param arr: array of integers to sort
    :param lo: lower bound of the array
    :param hi: higher bound of the array

    :return:
    """

    # Nothing to sort since we have only one element (or none)
    if lo >= hi:
        return

    # Find the position of the pivot
    p = partition_first_element(arr, lo, hi)

    # Recursively call this method on the left partition and on the right partition (without the pivot)
    _quicksort_first(arr, lo, p)
    _quicksort_first(arr, p+1, hi)


def partition_first_element(arr, lo, hi):
    """
    Partition the array by choosing the first element as a pivot.
    (This method is based on Sedgewick's quick sort implementation: https://algs4.cs.princeton.edu/23quicksort/)

    :param arr: The array of integers to partition
    :param lo: The lower boundary of the array
    :param hi: The higher boundary of the array

    :return:
    """
    pivot = arr[lo]

    # index cursor that walks through the array from left to right
    p_left = lo + 1

    # index cursor that walks through the array from right to left
    p_right = hi

    while (True):

        # advance the "left" cursor as long as the current element is smaller than the pivot
        while p_left <= hi and arr[p_left] < pivot:
            p_left += 1

        # advance the "right" cursor as long as the current element is bigger than the pivot
        while p_right >= lo+1 and arr[p_right] > pivot:
            p_right -= 1

        # the left and right cursor has passed each others, we can stop
        if (p_left >= p_right):
            break

        # switch the elements so the smaller element is on the right side and the bigger element is on the left side
        arr[p_left], arr[p_right] = arr[p_right], arr[p_left]

    # the "right" cursor is pointing to a "smaller" element, so we can switch with the pivot so the pivot is placed
    # at the right position.
    arr[p_right], arr[lo] = arr[lo], arr[p_right]

    return p_right


# Quicksort with first element as a pivot
arr = [5, 2, 6, 1, 3, 4]
print("Quicksort %s with first element as a pivot" % arr)
quicksort_first(arr)
print("=> %s" % arr)