'''
======================================================================================================================================================================================================================|
|                                                                                                                                                                                                                     |
|   Autor zadania: Hubert Miklas                                                                                                                                                                                      |
|   Złożoność czasowa algorytmu: O(n^2)                                                                                                                                                                           |
|   Złożoność pamięciowa algorytmu: O(p)                                                                                                                                                                              |
|   Gdzie n to ilość rzędów i kolumn w L                                                                                                                                                                              |
|   Opis algorytmu:                                                                                                                                                             
|   Zdefiniowałem funkcję f(i,j) czyli maksymalna ilość komnat odwiedzona w i-tej kolumnie na j-tej pozycji. Tłumacząc to na programowanie dynamicznie zauważam, że nie potrzebuję dwuwymiarowej tablicy, bo i tak 
|   Zaczynam od pierwszej kolumny, tam możemy pójść tylko w dół. Dla każdej następnej kolumny możęmy do danej komórki przejść na 3 sposoby - albo od lewej, bierzemy poprzednią 
|                                                                                                                                                                                                                     |
======================================================================================================================================================================================================================|
'''

from zad7testy import runtests


def maze(L):
    n = len(L)
    if L[0][0] == '#' or L[n-1][n-1] == '#':
        return -1
    
    down= [ -1 for j in range(n)]

    up = [-1 for j in range(n)]
    
    f = [ -float('inf') for j in range(n) ] 

    for i in range(n):
        if L[i][0] == "#":
            break
        f[i] = i

    for i in range(1,n):
        if(L[0][i] != "#"):
            if(L[0][i-1] != "#"):
                down[0] = f[0] + 1
            else:
                down[0] = -float('inf')
        else:
            down[0] = -float('inf')

        if(L[n-1][i] != "#"):
            if(L[n-1][i-1] != "#"):
                up[n-1] = f[n-1] + 1
            else:
                up[n-1] = -float('inf')
        else:
            up[n-1] = -float('inf')

        for j in range(1, n):
            if(L[j][i] == "#"):
                down[j] = -float('inf')
                continue
            if(L[j][i-1] != "#"):
                down[j] = max(down[j-1] + 1, f[j] + 1)
            else:
                down[j] = down[j-1] + 1

        for j in range(n-2, -1, -1):
            if(L[j][i] == "#"):
                up[j] = -float('inf')
                continue
            if(L[j][i-1] != "#"):
                up[j] = max(up[j+1] + 1, f[j] + 1)
            else:
                up[j] = up[j+1] + 1

        for j in range(n):
            f[j] = max(down[j], up[j])    
    return f[n-1] if f[n-1] != -float('inf') else -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )