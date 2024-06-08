
def can_make(A,T):
    n = len(A)
    dp = [ False for _ in range(T+1) ]
    for elem in A:
        dp[elem] = True
    for i in range(n):
        for elem in A:
            if elem + A[i] <= T and dp[i] == True:
                dp[i+elem] = True
    return dp[T]


