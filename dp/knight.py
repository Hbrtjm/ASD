

def magic(C):
    n = len(C)
    geld = [ -1 for _ in range(n) ]
    geld[0] = 0
    for i in range(n):
        if geld[i] > -1:
            for j in range(1,4):
                if C[i][j][0] <= C[i][0] + geld[i]:
                    geld[C[i][j][1]] = max(geld[C[i][j][1]],min( C[i][0] + geld[i] - C[i][j][0],10))
    return geld[n-1]