# TODO: implement sweeping

from random import randint
def compare(a,b):
    return a[0] < b[0]

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [(0,0)] * (n1)
    R = [(0,0)] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if compare(L[i],R[j]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

A = []
N = 10
for _ in range(N):
    k = randint(1,100)
    A.append((k,k+randint(1,100)))

C = [0] * N

mergeSort(A,0,len(A)-1)
print(A)

ans = 0

i = N - 1

while i > 0:
    if A[i][1] < A[i-1][1]:
        C[i-1] = C[i] + 1
        if C[i-1] > ans:
            ans = C[i-1]
    else:
        C[i-1] = C[i]
    i -= 1

print(C)
print(ans)