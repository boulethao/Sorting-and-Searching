#!/usr/bin/env python

class MyStack():
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if len(self.list) > 0:
            item = self.list.pop()
            return item
        else:
            raise "ERROR: Stack is empty."

    def isEmpty(self):
        return len(self.list) == 0


def iterative_quicksort(arr):
    """
    Iterative quicksort
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

    print (stack.list)


    while not stack.isEmpty():

        hi = stack.pop()
        lo = stack.pop()

        #as long as we have at least two elements to sort
        if lo < hi:

            #create the partitions
            p = partition(arr, lo, hi)

            #push the left partition indexes
            stack.push(lo)
            stack.push(p-1)

            # push the right partition indexes
            stack.push(p+1)
            stack.push(hi)


def partition(arr, lo, hi):
    """
    Last element pivot partition
    :param arr:
    :param lo:
    :param hi:
    :return:
    """
    pivot = arr[hi]
    i = lo
    j = lo

    while j <= hi:
        if (arr[j] < pivot):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1

    arr[i], arr[hi] = arr[hi], arr[i]

    return i

arr = [5, 2, 6, 1, 3, 4]
iterative_quicksort(arr)
print (arr)