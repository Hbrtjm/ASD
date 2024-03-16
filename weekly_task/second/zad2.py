from zad2testy import runtests

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
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

def b_search_find(T, x):
    l = 0
    r = len(T) - 1
    while l <= r:
        mid = (l + r) // 2
        if T[mid] < x:
            l = mid + 1
        elif T[mid] > x:
            r = mid - 1
        else:
            return mid  # Element is found
    return -1 

def b_search_find_greater(T, x):
    low = 0
    high = len(T)
    while low < high:
        mid = (low + high) // 2
        if T[mid] < x:
            low = mid + 1
        else:
            high = mid
    return low

def ksum(T, k, p):
    ans = 0
    p_list = [ T[i] for i in range(p) ]
    mergeSort(p_list,0,p-1)
    ans = p_list[p-k]
    print(p_list[p-k], end = " ")
    for i in range(0,len(T)-p):
        indx_insert = b_search_find_greater(p_list,T[i+p])
        # print(f"{indx_delete} {indx_insert}, ",end=" ")
        # print(f"{p_list},",end=" | ")
        p_list.insert(indx_insert,T[i+p]) 
        indx_delete = b_search_find(p_list,T[i])
        del p_list[indx_delete]
        # print(p_list[p-k], end = " ")
        ans += p_list[p-k]
    # tu prosze wpisac wlasna implementacje
    return ans


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
