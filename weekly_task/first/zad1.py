'''
    
    Autor zadania: Hubert Miklas
    Złożoność czasowa algorytmu: O(n * log k)
    Złożoność pamięciowa algorytmu: O(1) - nie liczbymy danych wejściowych

    Opis algorytmu:
    Dla k = Θ(1), k = Θ(log n) używając bubblesort, ponieważ w pierwszym przypadku funkcja czasu T(n) jest Θ(n), a dla k = Θ(log n) T(n) =  Θ(n * log n) co jest wystarczająco dobre. 
    Dla uzgodnienia, ktróy algorytm stosuję sprawdzam najpierw czy k*n nie przekracza 10^6, w innym razie, to jest dla k = Θ(n) należy już użyć merge sort lub innego algorytmu złożoności czasowej Θ(n * log n)
    w tym przypadku użyłem mergesort.
'''

from zad1testy import Node, runtests


def bubbleSort(pc,k):
    if pc is None or pc.next is None:
        return pc
    for _ in range(k):
        p = pc
        guard = Node()
        guard.next = p
        previous = guard
        while p.next != None:
            if p.val > p.next.val:
                if previous == guard:
                    temp = p.next
                    p.next = temp.next
                    temp.next = p
                    pc = temp
                    previous = temp
                    guard.next = temp
                else:
                    temp = p.next
                    p.next = temp.next
                    temp.next = p
                    previous.next = temp
                    previous = temp
            else:
                previous = p
                p = p.next
    return guard.next

def mergeSort(p,end=None):
    if p is None or p.next is None:
        return p
    mid = getMiddle(p)
    nmid = mid.next
    mid.next = None
    left = mergeSort(p,mid)
    right = mergeSort(nmid,end)
    sorted_list = merge(left, right)
    return sorted_list

def getMiddle(p):
    if p is None:
        return p
    slow = p
    fast = p
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(p1,p2,end=None):
    guard = Node()
    if p1.val > p2.val:
        guard.next = p1
        p1 = p1.next
    else:
        guard.next = p2
        p2 = p2.next
    current = guard.next
    while p2 != end or p1 != end:
        if p2 == end:
            current.next = p1
            current = current.next 
            break
        if p1 == end:
            current.next = p2
            current = current.next 
            break
        if p1.val < p2.val:
            current.next = p2
            current = current.next
            p2 = p2.next
        else:
            current.next = p1
            current = current.next
            p1 = p1.next
    return guard.next

def SortH(p,k):
    # p = bubblesort(p,k)
    n = 0
    current = p
    while current != None:
        n += 1
        current = current.next
    if  n * k  <= 10000:
        p = bubbleSort(p,k)
    else:
        p = mergeSort(p)
    print("Done")
    return p

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
