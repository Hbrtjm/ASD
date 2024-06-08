
def maxmin(A,k):
    n = len(A)
    table = [ [ 0 for _ in range(n) ] for _ in range(n)]
    for i in range(n):
        table[i][i] = A[i]
    for i in range(n):
        for j in range(i,n):
            table[i][j] = max()