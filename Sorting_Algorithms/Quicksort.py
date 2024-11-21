def partition(arr, h, t):
    pivot = arr[t] #constant amount of work
    i = h - 1 #constant amount of work

    for j in range(h, t): #time complexity is O(n)
        if arr[j] < pivot: #constant amount of work
            i += 1 #constant amount of work
            arr[i], arr[j] = arr[j], arr[i] #constant amount of work    
    
    arr[i + 1], arr[t] = arr[t], arr[i + 1] #constant amount of work

    return i + 1 #constant amount of work


def quickSort(arr, h, t):
    if h < t: #constant amount of work
        pivot_idx = partition(arr, h, t) #time complexity O(n)
        quickSort(arr, h, pivot_idx - 1)
        quickSort(arr, pivot_idx + 1, t)


arr = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]
length = len(arr)

print(f'Original array: {arr}\n')
quickSort(arr, 0, length - 1)
print(f'QuickSorted array: {arr}')

"""
Space complexity evaluates to O(1) - constant.

In the worse-case scenario (when data is chopped unbalanced),
the algorithm recurrence relation is T(n) = T(n - 1) + T(0) + O(n), 
where T(n - 1) is one leaf with n - 1 data and T(0) is another with ~0 data and finally O(n) is a for loop in 
a partition function.

                        n
                      /    \
                     0     n - 1
                          /    \
                         0      (n - 1) - 1
                                /   \
                               0     ((n - 1) - 1) - 1  

                    This evaluates to T(n) = n + (n - 1) + (n - 2) + (n - 3) + (n - 4) + ... 2 + 1,
                    which in turn is ∑ from 1 to n and equels to n(n + 1) / 2 (algebraic series).
                    Conclusively, n(n + 1) / 2 = n^2 = O(n^2).

The worse-case happens when the pivot element is the smallest or largest element in the array
or the array is already sorted and you choose first or last element as a pivot.


In the best-case scenario (when the data is chopped perfectly by half or just roughly) 
the recurrence relation is T(n) = 2T(n/2) + O(n) which evaluates to O(n*log(n)) (By master theorem).
The one like in MergeSort. The height of a tree is log(n) and each level is of n work, 
done by the loop in the partition function.

                        n
                    /       \
                  n/2       n/2
                /    \     /   \
              n/4   n/4  n/4   n/4
             .
            . 
           1 

The average-case is closer to best-case as opposed by worse-case, 
because even if the data are split into two halves proportionally uneven 
the resulting runtime will still be O(n*log(n)).              
Suppose, for example, that the partitioning algorithm always produces a 9-to-1
proportional split, which at first blush seems quite unbalanced. We then obtain the
recurrence: T(n) = T(9n/10) + T(n/10) + O(n). 
Every level of the tree has cost cn, 
until the recursion reaches a boundary condition at depth log10(n) = O(lg(n)), 
and then the levels have cost at most cn.
The recursion terminates at depth log10/9(n) = O(lg(n)). The total cost of Quicksort is therefore O(n*log(n)). 
Thus, with a 9-to-1 proportional split at every level of recursion, which intuitively seems quite unbalanced, 
Quicksort runs in O(n*log(n)) time — asymptotically the same as if the split was even for both halves. 
Even a 99-to-1 split yields an O(n*log(n)) running time. In fact, any split of constant
proportionality yields a recursion tree of depth O(lg(n))

In order to achieve an average-case, we could use Randomized Quicksort

    -> def randomized_partition(arr, h, p):
          import random 

          i = random.choice(arr)
          arr[p], arr[i] = arr[i], arr[p]
          return partition(arr, h, p)

Because we randomly choose the pivot element, we expect the split of
the input array to be reasonably well balanced on average.      
"""