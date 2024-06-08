
def tree( c ):
    n = len(c)
    dp = [ [0,0] for _ in range(n) ]
    dp[0][0] = c[0]
    for i in range(1,n):
        dp[i][0] = max(dp[i-1][1] + c[i],dp[i-1][0])
        dp[i][1] = max(dp[i-1][0],dp[i-1][1])
    return max(dp[n-1][0],dp[n-1][1])