def bubble_sort(arr):
    for _ in range(len(arr)): #this line has c amount of work, which is repeated n times.
        sorted = True #constant amount of work
        for k in range(len(arr) - 1): #this line has c amount of work, which is repeated n - 1 times (if optimazed then once).
            if arr[k] > arr[k + 1]: #constant amount of work
                arr[k], arr[k + 1] = arr[k + 1], arr[k] #constant amount of work
                sorted = False #constant amount of work
        
        if sorted: #constant amount of work
            break

    return arr

arr = [23, 1, 10, 5, 2]
print(bubble_sort(arr))

"""
The Bubblesort algorithms has the worse-case runtime of O(n^2), because it needs to run outer loop n times 
and inner loop n - 1 times (if not optimized). Space complexity is constant O(1) as doesn't require any auxilary space.
If the inner loop doesn't cause any swap over the first iteration, then the array is assumed to be already sorted, hence 
the runtime reduces to O(n)
""" 
