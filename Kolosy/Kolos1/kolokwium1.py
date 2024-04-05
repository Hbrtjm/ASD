'''
Autor zadania: Hubert Miklas
O(n^2): Dla każdego elementu przechodzimy w "tył" i sprawdzamy, ile jest takich, które są mniejsze od tego elementu
O(nlogn): Sortuję tablicę krotek zawierających wartość z tablicy i indeks tego elementu po wartościach mentów. 
Następnie przechodzę po tej tablicy i zapisuję jakie indeksy zostały napotkane używając binary insert, który zwraca. 
Rangą dla każgedo elementu będzie indeks indeksu w tablicy used_index. 
'''

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
    i = j = 0
    ans = []
    while i < len(L) and j < len(R):
        if L[i][0] < R[j][0]:
            ans.append(L[i])
            i+=1
        else:
            ans.append(R[j])
            j+=1
    while i < len(L):
        ans.append(L[i])
        i+=1
    while j < len(L):
        ans.append(L[j])
        j+=1
    return ans

def mergeSort(T):
    n = len(T)
    if n == 1:
        return T
    mid = n // 2
    L = T[mid:]
    R = T[:mid]
    mergeSort(L)
    mergeSort(R)
    return merge(L,R)

def binary_search(T,x):
    left = 0
    right = len(T) - 1
    while left <= right:
        mid = (left + right)//2
        if mid+1 < len(T):
            if x < T[mid+1] and x > T[mid-1]:
                return left
        if x < T[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return 0


def maxrank(T):
    n = len(T)
    table = [ (T[i],i)  for i in range(len(T)) ]
    # t = mergeSort(table)
    table.sort(key=lambda x: x[0])
    print(table)
    ans = 0
    temp = 0
    used_index = []
    for i in range(n):
        temp = binary_search(used_index,table[i][1])
        used_index.insert(temp,table[i][0])
        print(temp,end=" ")
        ans = max(temp,ans)
    return ans

T = [5,3,9,4]
print(solve_n2(T))
print(maxrank(T))