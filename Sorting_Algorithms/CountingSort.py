def counting_sort(arr):
    # Define the range k. When k = O(n), the CountSort run in O(n) time.
    k = max(arr) # O(n)
    # Coumt array of range k. 
    count_arr = [0] * (k + 1) # O(k). 
    # Output array of range n
    output_arr = [0] * len(arr) # O(n)
    
    # Count occurances of arr[i] element and store in count_arr.
    for i in range(len(arr)): # Order O(n)
        count_arr[arr[i]] += 1

    # Compute cummulative sum over count_arr. This helps determine the final
    # position of i-th value in output array.
    for i in range(1, k + 1): # Order O(k). Can say O(n)
        count_arr[i] = count_arr[i] + count_arr[i - 1]

    # Using count array we find a place for i-th element of input array.
    # And dicrement a count for i-th element's value of arr to make sure if the same value 
    # of arr is placed right before it   
    for i in range(len(arr) - 1, -1, -1): # Order O(n)
        output_arr[count_arr[arr[i]] - 1] = arr[i]
        count_arr[arr[i]] -= 1
        
    return output_arr

arr = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]    
print(counting_sort(arr))

"""
Counting Sort runs in O(k + n) time, which beats conventional O(nlog(n)) running time 
for comparison sorts. It manages to achieve this using counts of each i-th value of
an input array. First it allocated a count array which will hold counts of values 
of input array (O(k)). Afterwards we compute a cummulative sum over the count array, 
which tells us how many elements are lesser of equel to i-th element of an input array 
(O(k) -> O(n), if numerical difference between values is small. But generally it is O(n)) 
Lastly, we look up indeces of i-th element of an input array and place that element 
into an output array. Important to note, that we iterate an input array from backwards,
in order to preserve the stability.
In practice, we usually use counting sort when we have k = O(n), in
which case the running time is O(n)
"""
