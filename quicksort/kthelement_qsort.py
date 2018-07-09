def find_kth_element(a, lo, hi, k):
    """
    Find the k th element in the array (if it was sorted)
    :param a: the array of numbers
    :param lo: the lower bound of the array
    :param hi: the higher bound of the array
    :param k:  the rank of the element to be found
    :return: the kth element
    """
    if lo >= hi:
        return a[lo]

    p = partition(a, lo, hi)

    if (k-1) == p:
        return a[p]

    if (k - 1) < p:
        return find_kth_element(a, lo, p-1, k)

    if (k + 1) > p:
        return find_kth_element(a, p+1, hi, k)


def partition(a, lo, hi):
    """
    Last element pivot partition: rearrange elements in the array by putting all the elements < than pivot to the left
    and elements > than pivot to the right.
    :param a: array to partition
    :param lo: lower bound of the array to partition
    :param hi: higher bound of the array to partition
    :return: the final pivot position in the array
    """
    pivot = a[hi]
    i = lo
    j = lo

    while j <= hi:
        if (a[j] < pivot):
            a[i], a[j] = a[j], a[i]
            i += 1
        j += 1

    a[i], a[hi] = a[hi], a[i]

    return i


arr = [12, 3, 5, 7, 4, 19, 26]
item = find_kth_element(arr, 0, len(arr)-1, 2)
print(item)