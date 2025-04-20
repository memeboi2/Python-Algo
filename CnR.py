def combination_dp(n, r):
    """
    Calculate C(n,r) using dynamic programming approach
    Using Pascal's identity: C(n,r) = C(n-1,r-1) + C(n-1,r)
    """
    if r < 0 or r > n:
        return 0
    if r == 0 or r == n:
        return 1
    
    # Create a 2D array to store values
    dp = [[0 for _ in range(r + 1)] for _ in range(n + 1)]
    
    # Base cases
    for i in range(n + 1):
        dp[i][0] = 1
    
    for i in range(r + 1):
        dp[i][i] = 1
    
    # Fill dp table
    for i in range(1, n + 1):
        for j in range(1, min(i, r) + 1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    
    return dp[n][r]
