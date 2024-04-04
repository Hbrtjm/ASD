def b_search(A,start,finish,value):
    while start <= finish:
        mid = (start + finish)/2
        if A[mid] == value:
            return True
        elif A[mid] > value:
            finish = mid - 1
        else:
            start = mid + 1
    return False
def z3(A,x):
    n = len(A)
    for i in len(A):
        searched = A[i] - x
        if b_search(A,0,n,searched):
            return True
    return False