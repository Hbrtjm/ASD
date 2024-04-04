# zaimplementowac quick sort bez rekurencji
def quicksort(tab, p, k):
    stos = []
    while p < k:
        q = partition(tab, p, k)
        stos.append((p, q - 1))
        p = q
    while len(stos) > 0:
        krotka = stos.pop()
        p = krotka[0]
        k = krotka[1]
        q = partition(tab, p, k)
        if p < q:
            stos.append((p, q-1))

    return tab


def partition(A, p, r):
    # pivot = randint(p,r)
    # A[r],A[pivot]=A[pivot],A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= A[r]:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


# tab = [15,6,7,33,2,3,4]
tab = [3, 2, 1, 6, 99, 7]
quicksort(tab, 0, len(tab) - 1)
print(tab)
