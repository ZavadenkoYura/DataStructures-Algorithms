n = 4
prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

# A pure recursion solution which is very inefficient. The runtime is O(2^n)
# We try to solve the subproblem of a smaller size at each reccurent step (Recursion method)
def rod_cut_recursive(p, n):
    if n == 0: 
        return 0 # No profit

    optimal_revenue = float('-inf')

    for i in range(1, n + 1):
        optimal_revenue = max(optimal_revenue, p[i - 1] + rod_cut_recursive(p, n - i))

    return optimal_revenue

print(f"The result of {rod_cut_recursive.__name__} is {rod_cut_recursive(prices, n)}")

# Solving a rod cutting problem using recursion and tabulation for 
# optimizing the performance (Momoization method)
def rod_cut_recursive_memoized(p, n, memo={}):
    if n in memo:
        return memo.get(n)

    if n == 0: 
        return 0 # No profit

    optimal_revenue = float('-inf')

    for i in range(1, n + 1):
        # Computing the optimal revenue for n - i piece recursively
        compute_rod_length = rod_cut_recursive(p, n - i) 
        optimal_revenue = max(optimal_revenue, p[i - 1] + compute_rod_length)
        memo[n] = compute_rod_length

    return optimal_revenue

print(f"The result of {rod_cut_recursive_memoized.__name__} is {rod_cut_recursive_memoized(prices, n)}")


def rod_cut_bottom_up(p, n):
    memo = [0] * (n + 1)
    
    for i in range(1, n + 1):

        optimal_revenue = float('-inf')
        
        for j in range(1, i + 1):
            optimal_revenue = max(optimal_revenue, p[j - 1] + memo[i - j]) 
    
        memo[i] = optimal_revenue

    return memo[n]

print(f"The result of {rod_cut_bottom_up.__name__} is {rod_cut_bottom_up(prices, n)}")
