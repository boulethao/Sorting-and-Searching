#!/usr/bin/env python

class MyStack():
    """
    Simple stack implementation
    """
    def __init__(self):
        """
        Initialize the list of items of the stack
        """
        self.list = []

    def push(self, item):
        """
        Push an item onto the stack
        :param item: The item to push
        :return:
        """
        self.list.append(item)

    def pop(self):
        """
        Pop an item from top of the stack
        :return: The popped item
        """
        if len(self.list) > 0:
            item = self.list.pop()
            return item
        else:
            raise "ERROR: Stack is empty."

    def is_empty(self):
        """
        Check if the stack is empty
        :return: True if empty / False if not empty
        """
        return len(self.list) == 0


def iterative_quicksort(arr):
    """
    Iterative quick sort
    :param arr: arr to be sorted
    :return:
    """
    if arr is None or len(arr) <= 1:
        return

    lo = 0
    hi = len(arr)-1

    stack = MyStack()
    stack.push(lo)
    stack.push(hi)


    while not stack.is_empty():

        hi = stack.pop()
        lo = stack.pop()

        # as long as we have at least two elements to sort
        if lo < hi:

            # create the partitions
            p = partition(arr, lo, hi)

            # push the left partition indexes
            stack.push(lo)
            stack.push(p-1)

            # push the right partition indexes
            stack.push(p+1)
            stack.push(hi)


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


arr = [5, 2, 6, 1, 3, 4]
iterative_quicksort(arr)
print(arr)