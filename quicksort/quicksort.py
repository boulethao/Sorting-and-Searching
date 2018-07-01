# QUICKSORT

# Quicksort is a divide and conquer algorithm.
# It divides the array in two partitions by using as a reference a pivot:
#   - the left partition are values that are smaller than the pivot
#   - the right partition are values that are bigger than the pivot
# After the partition, the pivot will be placed at the right position.
# Repeat the sequence with the left partition then the right partition until all partitions are exhausted.
#
# Time complexity:
#   - partition is done in linear time
#   - repeating recursively the partition by removing the pivot at each level
#
#   Best: O(nlogn) if the pivot is always the middle of the array (left and right has the same amount of numbers)
#   Average: O(nlogn)
#   Worst: O(n^2) if the pivot is always the bigger or the smallest values
#
# Space complexity: O(1) in place
#
# Stable? No (swapping occurs between non adjacent elements)
#
# N.B.: Quicksort is usually faster than Mergesort.
#

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








# Quicksort with first element as a pivot
arr = [5, 2, 6, 1, 3, 4]
print("Quicksort %s with first element as a pivot" % arr)
quicksort_first(arr)
print("=> %s" % arr)

arr = [5, 2, 6, 1, 3, 4]
print("Quicksort %s with last element as a pivot" % arr)
quicksort_last(arr)
print("=> %s" % arr)

