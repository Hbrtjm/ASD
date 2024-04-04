def hoare(A, p, r):
    ind_left = p
    ind_right = r - 1
    while ind_left < ind_right:
        if A[ind_left] > A[r] and A[ind_right] < A[r]:
            A[ind_right], A[ind_left] = A[ind_left], A[ind_right]
            ind_left += 1
            ind_right -= 1
        elif A[ind_left] > A[r]:
            ind_right -= 1
        elif A[ind_right] < A[r]:
            ind_left += 1
        else:
            #oba dobre
            ind_right -= 1
            ind_left += 1
    A[ind_left], A[r] = A[r], A[ind_left]
    return ind_left


def quicksort(tab, p, k):
    while p < k:
        i = hoare(tab, p, k)
        if i - 1 - p > k - i:
            quicksort(tab, i + 1, k)
            k = i - 1
        else:
            quicksort(tab, p, i - 1)
            p = i + 1
    return tab


tab = [15, 6, 7, 33, 2, 3, 4]
quicksort(tab, 0, len(tab) - 1)
print(tab)
