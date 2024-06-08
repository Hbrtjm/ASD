
def moni(A,T):
    dp = [ float('inf') for _ in range(T+1) ]
    
    for elem in A:
        dp[elem] = 1
    
    for i in range(T+1):
        for elem in A:
            if i - elem > 0:
                dp[i] = min(dp[i],dp[i-elem]+1)
    print(dp)
    return dp[T]

money = [2,5]
amount = 19

print(moni(money,amount))