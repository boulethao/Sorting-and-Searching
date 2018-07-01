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

# Several implementation of Quicksort are available:
# - Method using first element as a pivot
# - Method using last element as a pivot
# - Method usging a random element as a pivot