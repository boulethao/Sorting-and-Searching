###
# QUICKSORT : RANDOM ELEMENT AS PIVOT
###

from my_random_generator import MyRandomGen

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
    Partition using a random number as a pivot. Switch this element with the last element in the array.
    Then proceed to the last element pivot partitioning
    :param arr:
    :param lo:
    :param hi:
    :return:
    """
    random_number = MyRandomGen().randomGen(lo, hi)

    #swap with the last element
    arr[random_number], arr[hi] = arr[hi], arr[random_number]

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

arr = [5, 2, 6, 1, 3, 4]
print("Quicksort %s with random element as a pivot" % arr)
quicksort(arr)
print("=> %s" % arr)