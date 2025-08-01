string = "character"
def longest_palindrom_sequence(s):
    dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]
        
    for i in range(1, len(s) + 1):
        for j in range(1, len(s) + 1):
            if s[i - 1] == s[-j]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len(s)][len(s)]

n = longest_palindrom_sequence(string)
print(n)