# Quick Sort 
  

#### Picking first or last element as a pivot

- Pros: 
    * easy to implement 
    * less overhead than other sorting algorithms
- Cons: 
    * take O(n<sup>2</sup>) if data is nearly sorted


##### First element: partition method based on 
[Lomuto's Partition Scheme](https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme)

```python

def partition(arr, lo, hi):
    
    pivot = arr[lo]
    p_left = lo + 1
    p_right = hi
    
    while (True):
    
        while p_left <= hi and arr[p_left] < pivot:
            p_left += 1

        while p_right >= lo+1 and arr[p_right] > pivot:
            p_right -= 1
    
        if (p_left >= p_right):
            break
    
        arr[p_left], arr[p_right] = arr[p_right], arr[p_left]

    
    arr[p_right], arr[lo] = arr[lo], arr[p_right]
    
    return p_right
    
```

<img src="./images/quicksort-1stelement-pivot.png"
alt="Partitioning with first element as pivot" width="70%" height="70%" border="10" /></a>



##### Last element: partition method Based on 
[Hoare’s Partition Scheme](https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme) 
or [Sedgewick's implementation](https://algs4.cs.princeton.edu/23quicksort/)


```python

def partition(arr, lo, hi):

    pivot = arr[hi]

    index = lo

    p = lo - 1

    while index < hi:

        if arr[index] < pivot:
            p += 1
            arr[index], arr[p] = arr[p], arr[index]

        index += 1

    p += 1
    arr[hi], arr[p] = arr[p], arr[hi]

    return p
    
```
<img src="./images/quicksort-lastelement-pivot.png"
alt="Partitioning with last element as pivot" width="70%" height="70%" border="10" /></a>


#### Picking a random element as a pivot

- Pros: 
    * helps improving the chance of getting a time complexity of __O(n log n)__ instead of __O(n<sup>2</sup>)__
    * less overhead than other sorting algorithms.
- Cons: 
    * random generator can be slow and can still give a runtime of __O(n<sup>2</sup>)__ (but most unlikely)

The quick sort implementation is as simple as implementing a random generator and reusing the partition implementation 
using the first/last element as a pivot.

Here is an example of a random generator using the combination of random bits: 
[My Random Generator](./my_random_generator.py)



#### Picking the median of three elements

- Pros: 
    * easy to implement
    * faster to calculate than random pivot method (but slower than the first/last element pivot method)
    * better choice of pivot when array is nearly sorted
- Cons:
    * runtime can still be __O(n<sup>2</sup>)__ if unlucky
    
Median-of-three method picks the first, last and middle elements of the array and calculate the median of all three.
After choosing the median, we switch with the first element or the last element of the array and proceed as usual for
partitioning (first/last element pivot):








