s1 = "stone"
s2 = "longest"

# Runtime is O(n^2)
def lcs_top_down(i, j, s1, s2, mem={}):    
    # Recurance Relation (Top-Down Approach)
    """
        s1.len or s2.len is 0 -> 0
        s1[i] != s2[j] -> max(lcs_recurvice(s1[i+1], s2[j]), s1[i], s2[j+1])
        s1[i] == s2[j] -> 1 + lcs_recurvice(s1[i+1], s2[j+1])
    """
    if (i, j) in mem:
        return mem[(i, j)]
    
    if i >= len(s1) or j >= len(s2):
        return 0
    
    if s1[i] == s2[j]:
        mem[(i, j)] = 1 + lcs_top_down(i + 1, j + 1, s1, s2)
        return mem[(i, j)] 

    if s1[i] != s2[j]:
        mem[(i, j)] = max(lcs_top_down(i, j + 1, s1, s2), lcs_top_down(i + 1, j, s1, s2))
        return mem[(i, j)] 
        
# print(lcs_top_down(0, 0, s1, s2))


# Runtime is O(m + n)
def lcs_bottom_up(s1, s2):    
    table = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                table[i][j] = 1 + table[i - 1][j - 1]
            else: 
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    return table[len(s1)][len(s2)]

print(lcs_bottom_up(s1, s2))