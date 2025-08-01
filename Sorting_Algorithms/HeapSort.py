""" 
Maintains max heap property at node i. 
Heapify charachterizes itself by the following recurrence relation: T(n) = T(2n/3) + O(1), where O(1) is the swap operation
and T(2n/3) is the recursive call. Each time the recursion does down, it reduces the n by approximately 2/3, which is the most nodes in the subtree (worse-case).  
"""
def max_heapify(arr, length, i):
    largest = i #constant amount of work
    left = (i * 2) + 1 #constant amount of work
    right = (i * 2) + 2 #constant amount of work

    if left < length and arr[left] > arr[largest]: #constant amount of work
        largest = left #constant amount of work

    if right < length and arr[right] > arr[largest]: #constant amount of work
        largest = right #constant amount of work

    if largest != i: #constant amount of work
        [arr[i], arr[largest]] = [arr[largest], arr[i]] #constant amount of work
        #tail recursion which doesn't return from the call stack.
        #the time complexity is O(log n) due to the height of the heap.
        #the space complexity is O(log n) due to the recursive call stack depth.
        max_heapify(arr, length, largest) 

"""
Builds max heap. Begins from the half of the array as those elements are the last non-leaf nodes.
Complexity: The loop iterates approximately O(n/2) times so O(n). Although MAX-HEAPIFY runs in O(log(n)) time for each node, 
not all nodes are at the same depth. Nodes closer to the bottom of the tree 
are processed with less work compared to nodes closer to the root. Despite MAX-HEAPIFY being 
O(log(n)) for individual nodes, the total complexity for building the heap is 
O(n), due to the decreasing amount of work required for nodes at lower levels of the heap.
"""
def build_max_heap(arr, length):
    for i in range(length//2-1, -1, -1): # O(n/2) so just O(n) amount of work
        max_heapify(arr, length, i)

"""
Sorts the max heap by taking into account the fact that the root element is the largest. 
It swaps the root with the last node and then runs max_heapify
to maintain max heap property but now on the reduced heap (last element exluded, because now sorted).
    -> O(build_max_heap) + (n-1) * O(max_heapify) = O(n) + O(n - 1 * log(n)) = O(2nlog(n)) = O(n*log(n))
"""
def heap_sort(arr, length):
    build_max_heap(arr, length) # amount of word done is O(n)
    for i in range(length - 1, 0, -1): # amount of word done is O(n)
        [arr[0], arr[i]] = [arr[i], arr[0]] #constant amount of work
        max_heapify(arr, i, 0)  #the time complexity is O(log n) due to the height of the heap.

    return arr

arr = [5, 3, 17, 10, 84, 19, 6, 22]
length = len(arr)


"""" Implementation of a Priority queue using max heap """
"""
    1. MAXIMUM function returns the element with the largest key (root element of a max heap). (Time complexity is O(1) constant data access)
    2. EXTRACT_MAX removes the biggest element (root). It first swaps root element with the last element then reduces heap size by one.
        Finally performs max-heapify to maintain heap property. (Time complexity is O(log(n)), because of heapify) 
    3. HEAP_INCREASE_KEY increases the value of a node by one. From that node it then traverses towards its parent 
        and swaps the values if bigger until the very root. (The worse-case time complexity is O(log(n), if the node whose value is being increased, is at the very bottom))
    4. MAX-HEAP-INSERT increases the heap size by one and puts the element with its priority (key) in the last position. Afterwards the function calls HEAP_INCREASE_KEY 
        which in turn propagates that element upwards if it's bigger then its parent. (The time complexity is O(log(n)) since a new element is always inserted at the end, meaning
        HEAP_INCREASE_KEY will need to go through whole height h of the heap with nodes n)
"""

def get_maximum(max_heap_array):
    return max_heap_array[0] #constant amount of work


def extract_max(max_heap_array):
    heap_size = len(max_heap_array)

    if heap_size < 1:
        print('No elements in the heap -> [HEAP UNDERFLOW]')
        return
    
    # Swap the root node with the last node
    max_heap_array[0], max_heap_array[heap_size - 1] = max_heap_array[heap_size - 1], max_heap_array[0]
    max_heap_array.pop()

    max_heapify(max_heap_array, heap_size - 1, 0)

    return max_heap_array


def increase_key(max_heap_array, idx, key):
    if max_heap_array[idx] > key: #constant amount of work
        print('The provided key is smaller') #constant amount of work  
        return

    max_heap_array[idx] = key #constant amount of work

    k = idx #constant amount of work
    parent = (idx - 1) // 2 #constant amount of work
    while k > 0 and max_heap_array[parent] < max_heap_array[k]: #At worse-vase repeates O(log(n)) times.
        max_heap_array[k], max_heap_array[parent] = max_heap_array[parent], max_heap_array[k] #constant amount of work
        k = parent #constant amount of work
        parent = (k - 1) // 2 #constant amount of work


def insert(max_heap_array, key):
    max_heap_array.extend([0]) #constant amount of work 
    increase_key(max_heap_array, len(max_heap_array) - 1, key) #At worse-vase repeates O(log(n)) times.

