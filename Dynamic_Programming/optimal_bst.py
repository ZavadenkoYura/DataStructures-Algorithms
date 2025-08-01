def optimal_bst(keys, p, q):
    n = len(keys)
    e = [[0] * (n + 2) for _ in range(n + 2)]   # e[i][j]: expected cost from key i+1 to j
    w = [[0] * (n + 2) for _ in range(n + 2)]   # w[i][j]: sum of p[i]..p[j-1] + q[i]..q[j]
    root = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        e[i][i] = q[i]
        w[i][i] = q[i]

    # l = length of the subtree (1 to n)
    for l in range(1, n + 1):
        for i in range(n - l + 1):
            j = i + l
            e[i][j] = float('inf')
            w[i][j] = w[i][j - 1] + p[j - 1] + q[j]
            for r in range(i + 1, j + 1):  # candidate roots
                cost = e[i][r - 1] + e[r][j] + w[i][j]
                if cost < e[i][j]:
                    e[i][j] = cost
                    root[i][j - 1] = r

    return e, root

keys = ['A', 'B', 'C', 'D', 'E', 'F']
p = [0.05, 0.4, 0.08, 0.04, 0.1, 0.33]
q = [0.06, 0.03, 0.05, 0.02, 0.04, 0.01, 0.03]

e, root = optimal_bst(keys, p, q)
