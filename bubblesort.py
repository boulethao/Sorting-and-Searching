# BUBBLE SORT

# Starting from the end of the array
# Swap the first element if it's smaller than the element at its previous index
# Repeat on the next pair down to the beginning of the array
# At the 1st iteration, the smallest element is allocated at the beginning of the array,
# At the 2nd one at the next index, and so on.

# Time complexity:
#   best: O(n) if nearly sorted
#   average: O(n^2)
#   worst: O(n^2) when array is reversed

# Space complexity: O(1)

# Stable? Yes

def bubblesort(arr):
    """
    Bubble sort an array of integers
    :param arr (list):  Array of integers
    :return:
    """

    if arr is None and len(arr) <= 1:
        return arr

    n = len(arr)

    for i in range (n):

        swapped = False

        for j in range (n-1, i, -1):
            # swap the pair if the 2nd elemnt [j-1] is smaller than the 1st one [j]
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swapped = True

        # stop if there is no need to sort
        if swapped is False:
            break




# Run bubble sort
arr = [64, 34, 25, 12, 22, 1, 90]
bubblesort(arr)
print(arr)