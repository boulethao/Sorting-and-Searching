###
# QUICKSORT : MEDIAN OF THREE ELEMENT AS PIVOT
###


def quicksort(arr):
    """
    Quicksort by choosing the last element in the array as a pivot

    :param arr: array of integers to sort

    :return:
    """
    if arr is None or len(arr) <= 1:
        return

    _quicksort(arr, 0, len(arr)-1)


def _quicksort(arr, lo, hi):
    """
    This method is recursively called after partitioning the array.

    The partition method chooses a pivot (last element) and divides the array into two sub-arrays.
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
    p = partition(arr, lo, hi)

    # Recursively call this method on the left partition and on the right partition (without the pivot)
    _quicksort(arr, lo, p)
    _quicksort(arr, p+1, hi)


def partition(arr, lo, hi):
    """
    Partition by choosing the median of three elements (first, middle and last element of the array) as a pivot.
    Switch this element with the last element in the array.
    Then proceed to the last element pivot partitioning
    :param arr:
    :param lo:
    :param hi:
    :return:
    """

    medianIndex = getMedianIndex(arr, lo, (lo+hi)//2, hi)

    #swap the median element with the last element
    arr[hi], arr[medianIndex] = arr[medianIndex], arr[hi]

    #and proceed to the partition

    pivot = arr[hi]

    i = lo - 1
    j = lo

    while j < hi:

        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

        j += 1

    i += 1
    arr[hi], arr[i] = arr[i], arr[hi]

    return i


def getMedianIndex(arr, e1, e2, e3):
    """
    Get the index of the median of three elements in an array
    :param: arr: the array
    :param e1: one of the three elements
    :param e2: one of the three elements
    :param e3: one of the three elements
    :return: median of the three elements
    """

    # smaller_element <= median <= larger_element
    # <=>
    # larger_element - median >= 0


    # ALSO

    # smaller_element <= median <= larger_element
    # <=>
    # smaller_element - median <= 0
    # <=>
    # median - smaller_element >= 0
    #
    #

    # in order to make an operation with two values and get a positive result, we need to
    # multiple two positive numbers or multiply two negative numbers

    # In this case, we need to take as an assumption that one of the element is a median and use the multiplication
    # operation to find out if the chosen element is really the median

    # hypothesis 1: median = e1
    factor1 = arr[e2] - arr[e1]
    factor2 = arr[e1] - arr[e3]

    if (factor1 * factor2) >= 0:
        return e1

    # hypothesis 2: median = e2
    factor1 = arr[e1] - arr[e2]
    factor2 = arr[e2] - arr[e3]

    if (factor1 * factor2) >= 0:
        return e2

    return e3



arr = [5, 2, 6, 1, 3, 4]
print("Quicksort %s with median-of-three elements as a pivot" % arr)
quicksort(arr)
print("=> %s" % arr)