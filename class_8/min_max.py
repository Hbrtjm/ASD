def matrix_multiply(A):
    n = len(A)
    dp = [ [ 0 for _ in range(n) ] for _ in range(n) ]
    current_matrix = [ [ (0,0) for _ in range(n) ] for _ in range(n) ]
    for i in range(n):
        current_matrix[i][i] = A[i]
    for i in range(n-1,-1,-1):
        for j in range(i,n-1):
            dp[j][j] = i