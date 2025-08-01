def insertion_sort(arr):
    for i in range(1, len(arr)): #this line has c amount of work, which is repeated n - 1 times.
        curr_val = arr[i] #constant amount of work
        k = i - 1 #constant amount of work

        while k >= 0 and arr[k] >= curr_val: #this line has c amount of work, and runs up to O(n) times at worst case.
           arr[k + 1] = arr[k] #constant amount of work
           k = k - 1  #constant amount of work

        arr[k + 1] = curr_val #constant amount of work

    return arr

arr = [23, 1, 10, 5, 2]
print(insertion_sort(arr))

""""
The worse running time of this algorithms if O(n^2) and time complexity is constant O(1) 
meaning that the storage capacity doesn't grow as an input size gets bigger, since it sorts in-place. 
Outer loop with pointer i runs through the whole array, while inner pointer k is always smaller k <= i.
Pointer k decreases from i. 
When the inner pointer (while loop) k encounters 0 or element arr[k] finds smaller element then curr_val, it starts to copy elements ahead-wise,
and at the end find the position where to place curr_val under the index k + 1. 
"""
