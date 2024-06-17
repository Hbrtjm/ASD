from egz2btesty import runtests


def magic(C):
    n = len(C)
    geld = [ -1 for _ in range(n) ] # [ [-1 for i in range(10) ] for _ in range(n) ]
    geld[0] = 0
    for i in range(n):
        if geld[i] > -1: # The chamber can be reached
            for j in range(1,4): 
                if C[i][j][0] <= C[i][0] + geld[i] and C[i][j][1] != -1 and i < C[i][j][1] and 10 >= C[i][0] - C[i][j][0]: # Can't visit a chamber with not enough gold, some of the doors don't work and if we go backwards, we die
                    geld[C[i][j][1]] = max(geld[C[i][j][1]],geld[i] + C[i][0] - C[i][j][0])
    if n < 30:
        for i in range(n):
            print(f"{i} {C[i]}")
        print(geld)
    return geld[n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
