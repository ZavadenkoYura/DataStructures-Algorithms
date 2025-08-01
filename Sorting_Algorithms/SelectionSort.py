"""
This implementation of a selection sort is unstable, meaning it doesn't preserve a relative order of similar elements 
of the input data (even though it's not such a big deal with integers, it can violate data integrity when performed on data (id, name) tuples)
"""

def selection_sort(arr):
    for i in range(len(arr)): #this line of code has amount of work c, which is repeated n times
        min_idx = i #constant amount of work
        for k in range(i + 1, len(arr)): #this line of code has amount of work c, which is repeated n - i - 1 times
            if arr[min_idx] > arr[k]:
                min_idx = k #constant amount of work

        arr[i], arr[min_idx] = arr[min_idx], arr[i] #constant amount of work

    return arr

arr = [23, 64, 25, 12, 22, 11]
print(selection_sort(arr))

"""
The Selection sort run in O(n^2) and doesn't require any additional auxilary space as the input size grows, 
so it's O(1) - constant. Outer loop runs total n times, whereas inner loop n - i - 1 times, since it runs off the i-th element.
Outer loop stops at one element at a time and then the inner one looks for the smallest element of the unsorted portion of the array. 
If it finds one it swaps it with the current smallest element localed at i-th index.
"""



"""
This implementation is stable, meaning it preserves a relative order of similar elements.
Stability in Selection sort can be achieved through a similar technique like in Insertion sort - shifting instead of swapping. 
"""

def stable_selection_sort(arr):
    # To come
    return arr

print("Stable Selection Sort: ", stable_selection_sort(arr))