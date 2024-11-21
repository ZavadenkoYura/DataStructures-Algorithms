def merge(left, right):
    output_arr = [] #space complexity O(n)
    left_ptr = 0  #constant amount of work
    right_ptr = 0  #constant amount of work

    while left_ptr < len(left) and right_ptr < len(right): #time complexity O(n)
        if left[left_ptr] < right[right_ptr]: 
            output_arr.append(left[left_ptr])  #constant amount of work
            left_ptr = left_ptr + 1 #constant amount of work
        else:
            output_arr.append(right[right_ptr]) #constant amount of work
            right_ptr = right_ptr + 1  #constant amount of work
        
    while left_ptr < len(left): #time complexity O(n)
        output_arr.append(left[left_ptr])  #constant amount of work
        left_ptr = left_ptr + 1  #constant amount of work

    while right_ptr < len(right): #time complexity O(n)
        output_arr.append(right[right_ptr])  #constant amount of work
        right_ptr = right_ptr + 1  #constant amount of work

    return output_arr


def merge_sort(arr):    
    if len(arr) <= 1:
        return arr #constant amount of work

    mid = len(arr) // 2 #constant amount of work

    left = merge_sort(arr[:mid]) #Recursive call: T(n/2)
    right = merge_sort(arr[mid:]) #Recursive call: T(n/2)

    return merge(left, right) #The amount of work is O(n)

arr = [23, 1, 10, 5, 2, 12, 4]
print(merge_sort(arr))


""""
Merge sort at best- average- and worse-case runs O(n*log(n)). The equation type of Merge sort is T(n) = aT(n/b) + f(n).
Where aT(n/b) corresponds to devide part (a number of subproblems and b subproblem size) 
and f(n) to conquer/combine parts which are constant in runtime. This algorithm devides an array of size n into smaller parts
using recursion (n/2^i) until array size is of 1 element. Then simply merges the two arrays.
T(n) = aT(n/b) + f(n) can be solved either using Tree method or Master theorem.
Using Master Theorem - n^logb(a) and f(n) are of the same size (since n^log2(2) = n, f(n) = n) 
so the solution is O(n^logb(a) * log(n)) which is O(nlog(n)).
Compared to other algorithms Merge sort is quite efficient on large datasets.
"""