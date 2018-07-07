# QUICK SELECT

import random

def quickselect(arr, k):
    """
    :param arr:
    :param k:
    :return:

    Method to find the smallest kth element in an unordered array

    @param arr: array of unordered numbers
    @param k: cardinality of the element if the array was ordered.

    @return: the smallest kth element
    """

    if arr is None or len(arr) == 0:
        return None

    return _quickselect(arr, 0, len(arr) - 1, k)


def _quickselect(arr, lo, hi, k):
    """
    Finds the smallest kth element in thearray.
    Using the partition method, select a pivot and finds its position if
    the array was ordered
        - If the position is k, then return the element at that position
        - If position < k, recursive call to _quickselect on the left portion of the partition
        - If position < k, recursive call to _quickselect on the right portion of the partition

    @param arr: array of numbers
    @param lo: lower bound of the array
    @param hi: higher bound of the array
    @param k: cardinality of the element if the array was ordered.

    return: the element at k-1th position if the array was sorted
    """

    if lo >= hi:
        return arr[lo]



    p = partition(arr, lo, hi)
    print("p is %s" %p)

    if k == p:
        return arr[k]

    if k < p:
        return _quickselect(arr, lo, p - 1, k)

    return _quickselect(arr, p + 1, hi, k)


def partition(arr, lo, hi):
    """
    Partitions the array (delimited by the lower bound lo and higher bound hi)
    in two portions by chosing a random pivot and placing that pivot at it's position if the array was ordered

    @param arr: array of numbers
    @param lo: lower bound of the array
    @param hi: higher bound of the array

    """

    print ("lower bound %s" %lo)
    print("higher bound %s" % hi)

    index = random.randint(lo, hi)
    print("random index %s" % index)

    #proceed to Hoare's partition scheme by swapping with last element
    arr[index], arr[hi] = arr[hi], arr[index]

    pivot = arr[hi]

    i = lo-1
    j = lo

    while (j < hi):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

        j += 1

    i += 1
    arr[i], arr[hi] = arr[hi], arr[i]

    return i


arr = [5, 2, 6, 1, 3, 4]
k = 3
print("Find %sth element in the array" % k)
kthelement = quickselect(arr, k)
print("=> %s" % kthelement)
