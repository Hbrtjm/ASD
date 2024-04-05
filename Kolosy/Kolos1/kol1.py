'''
Autor zadania: Hubert Miklas
Złożoność obliczeniowa O(n^2) złożoność pamięciowa O(1): Dla każdego elementu przechodzimy w "tył" i sprawdzamy, ile jest takich, które są mniejsze od tego elementu
Złożoność obliczeniowa O(nlogn) Złożoność pamięciowa O(n): Sortuję tablicę krotek zawierających wartość z tablicy i indeks tego elementu po wartościach mentów. 
Następnie przechodzę po tej tablicy i zapisuję jakie indeksy zostały napotkane używając binary insert (więc wyszukanie elementu O(logn), dla każdego
elementu, więc dla n elementów ogółem O(nlogn)), który zwraca. Rangą dla każgedo elementu będzie indeks indeksu w tablicy used_index. 
Sortuję tablicę mergesortem, który najpierw bierze pod uwagę wartość elementu, a później jego indeks, przy czym indeks sortuje malejąco, 
by nie zliczać elementu o tej samej wartości. Tu tak samo binary_search działa złożoności czasowej O(logn) i dla każdego elementu wyszukujemy indeks.
table.insert działa w oczekiwanym czasie stałym O(1). Ostatecznie złożoność obliczeniowa to O(nlogn)
'''

from kol1testy import runtests

def solve_n2(T):
    ans = 0
    for i in range(len(T)):
        temp = 0
        for j in range(i,-1,-1):
            if T[j] < T[i]:
                temp += 1
        ans = max(ans,temp)
    return ans

def merge(L,R):
    i = 0
    j = 0
    ans = []
    while i < len(L) and j < len(R):
        if L[i][0] < R[j][0]:
            ans.append(L[i])
            i+=1
        elif L[i][0] > R[j][0]:
            ans.append(R[j])
            j+=1
        else:
          if L[i][1] > R[j][1]:
              ans.append(L[i])
              i+=1
          elif L[i][1] < R[j][1]:
              ans.append(R[j])
              j+=1
    while i < len(L):
        ans.append(L[i])
        i+=1
    while j < len(R):
        ans.append(R[j])
        j+=1
    return ans

def mergeSort(T):
    n = len(T)
    if n == 1:
        return T
    mid = n // 2
    L = T[mid:]
    R = T[:mid]
    L = mergeSort(L)
    R = mergeSort(R)
    return merge(L,R)

def binary_search(T, x):
    left = 0
    right = len(T)
    while left < right:
        mid = (left + right) // 2
        if T[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left



def maxrank(T):
    n = len(T)
    table = [ (T[i],i)  for i in range(len(T)) ]
    table = mergeSort(table)
    # print(table)
    ans = 0
    temp = 0
    used_index = []
    for i in range(n):
        temp = binary_search(used_index,table[i][1])
        used_index.insert(temp,table[i][1])
        ans = max(temp,ans)
    return ans
    # ans = 0
    # for i in range(len(T)):
    #     temp = 0
    #     for j in range(i,-1,-1):
    #         if T[j] < T[i]:
    #             temp += 1
    #     ans = max(ans,temp)
    # return ans
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )
