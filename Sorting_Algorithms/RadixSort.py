def counting_sort(arr, div):
    count_arr = [0] * 10 # auxilary space is O(1)
    output_arr = [0] * len(arr) # auxilary space is O(n)
    
    for i in range(len(arr)): # runtime is O(n)
        charge = arr[i] // div # constant amount
        count_arr[charge % 10] += 1 # constant amount

    for i in range(1, 10): # runs ten time, so O(1)
        count_arr[i] += count_arr[i - 1] # constant amount

    for i in range(len(arr) - 1, -1, -1): # runtime is O(n)
        charge = arr[i] // div # constant amount
        output_arr[count_arr[charge % 10] - 1] = arr[i] # constant amount
        count_arr[charge % 10] -= 1 # constant amount
        
    for i in range(0, len(arr)): # runtime is O(n)
        arr[i] = output_arr[i] # constant amount
        

def radix_sort(arr):
    element = max(arr) # constant amount O(1) (In practice, but in theory O(n)) 
    div = 1 # constant amount O(1)
    
    while element // div > 0: # will execute d times, where d = b / r. d is a number of digits, b is a number of bits to represent the whole number 
        # and r is a number of bits for a single digit. If b = 32, r = 8 then the number of digits d is 4 
        counting_sort(arr, div) # Runs in O(n + k), where k = 2^r - 1
        div *= 10 # Constant amount of time
    
    return arr    
    

arr = [631, 232, 432, 121, 125, 776, 345]    
print(radix_sort(arr))


"""
The Radix sort runtime is equel to O(d(n + k)), where d is a number of digits to sort on, (n + k) is the runtime of the Counting Sort
For a value r <= b, we view each key as having d = b/r digits of r bits
each. Each digit is an integer in the range 0 to 2^r - 1, so that we can use counting
sort with k = 2^r - 1. (For example, we can view a 32-bit word as having four 8-bit
digits, so that b = 32, r = 8, k = 2r - 1 = 255, and d = b/r = 4.) Each pass of
counting sort takes time O(n + k) = O(n + 2^r) and there are d passes, for a total
running time of O(d(n + 2^r)) = O((b/r) * (n + 2^r))

If b < log(n) -> Process all bits in one pass (r = b), achieving O(n) runtime
If b >= log(n) -> Process log(n) bits per pass (r = log(n)), achieving O(bn / log(n)) runtime

"""