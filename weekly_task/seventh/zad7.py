from zad7testy import runtests


def maze(L):
    n = len(L)
    if L[0][0] == '#' or L[n-1][n-1] == '#':
        return -1
    
    d = [ -1 for j in range(n)]

    u = [-1 for j in range(n)]
    
    f = [[ -float('inf') for j in range(n) ] for i in range(n) ]

    for i in range(n):
        if L[i][0] == "#":
            break
        f[i][0] = i

    for i in range(1,n):
        if(L[0][i] != "#"):
            if(L[0][i-1] != "#"):
                d[0] = f[0][i-1] + 1
            else:
                d[0] = -float('inf')
        else:
            d[0] = -float('inf')

        if(L[n-1][i] != "#"):
            if(L[n-1][i-1] != "#"):
                u[n-1] = f[n-1][i-1] + 1
            else:
                u[n-1] = -float('inf')
        else:
            u[n-1] = -float('inf')

        for j in range(1, n):
            if(L[j][i] == "#"):
                d[j] = -float('inf')
                continue
            if(L[j][i-1] != "#"):
                d[j] = max(d[j-1] + 1, f[j][i-1] + 1)
            else:
                d[j] = d[j-1] + 1

        for j in range(n-2, -1, -1):
            if(L[j][i] == "#"):
                u[j] = -float('inf')
                continue
            if(L[j][i-1] != "#"):
                u[j] = max(u[j+1] + 1, f[j][i-1] + 1)
            else:
                u[j] = u[j+1] + 1

        for j in range(n):
            f[j][i] = max(d[j], u[j])

    if(n < 15):   
        for i in range(n):
            print(f[i])
    
    return f[n-1][n-1] if f[n-1][n-1] != -float('inf') else -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )