n = 4

def fibonacci(n, mem={}):
    if n in mem:
        return mem[n]
    
    if (n <= 1):
        return n
    
    mem[n] = fibonacci(n - 2) + fibonacci(n - 1) 
    return mem[n]

print([fibonacci(i) for i in range(1, 10)])