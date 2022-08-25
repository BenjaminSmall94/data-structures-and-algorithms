# Blog Notes: Quick Sort

## QuickSort

Quick sort is a sorting algorithm that employs to the divide and conquer method exploit the fact that sorting small lists and then merging these presorted lists runs drastically faster than sorting large amounts of random data at the same time. It does this using a pivot and swap method.

[QuickSort](../../python/code_challenges/quicksort.py)

### Pseudocode

![Insertion Sort Pseudo Code 1](quicksort_pseudo_1.png)
![Insertion Sort Pseudo Code 2](quicksort_pseudo_2.png)

### Trace

Sample Array: `[8, 4, 23, 42, 16, 15]`

![Quicksort Trace](quicksort_trace.png)


### Efficiency

- Time: O(n*log(n))
  - The for every element in the array it performs an average of n/2 comparisons and swaps so more specifically O(n^2/2)
- Space: O(n)
  - Because a stack of space 'n' is generated during the recursion to the base case

### Testing

[Testing File](../../python/tests/code_challenges/test_quicksort.py)
