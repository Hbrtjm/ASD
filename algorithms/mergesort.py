def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        arr[:] = merge(L, R)


def merge(l, r):
    ans = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            ans.append(l[i])
            i += 1
        else:
            ans.append(r[j])
            j += 1
    while i < len(l):
        ans.append(l[i])
        i += 1
    while j < len(r):
        ans.append(r[j])
        j += 1

    return ans
