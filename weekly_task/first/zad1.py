'''
======================================================================================================================================================================================================================|
|                                                                                                                                                                                                                     |
|   Autor zadania: Hubert Miklas                                                                                                                                                                                      |
|   Złożoność czasowa algorytmu: O(n * k) dla małych przypadków, O( n * log n ) dla dużych                                                                                                                            |
|   Złożoność pamięciowa algorytmu: O(1)                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
|   Opis algorytmu:                                                                                                                                                                                                   |
|   Dla k = Θ(1), k = Θ(log n) używając bubblesort, ponieważ w pierwszym przypadku funkcja czasu T(n) jest Θ(n), a dla k = Θ(log n) T(n) =  Θ(n * log n) co jest wystarczająco dobre.                                 |
|   Dla uzgodnienia, który algorytm stosuję sprawdzam najpierw czy k*n nie przekracza 5*10^6, w innym razie, to jest dla k = Θ(n), należy już użyć merge sort lub innego algorytmu złożoności czasowej Θ(n * log n)   |
|   bez konieczności brania k pod uwagę, bo w takim przypadku k jest na tyle duże, że różnica między O(n*log(k)) i O(n*log(n)) jest niewielka [zakładając, że istnieje algorytm o złożoności O(n*log(k))].            |
|   W tym przypadku użyłem mergesort, bo był najbardziej intuicyjny w implementacji.                                                                                                                                  |
|                                                                                                                                                                                                                     |
======================================================================================================================================================================================================================|
'''

from zad1testy import Node, runtests

def bubbleSort(pc,k):
    if pc == None or pc.next == None:
        return pc
    p = pc
    guard = Node()
    guard.next = p
    for _ in range(k):
        previous = guard
        p = guard.next
        while p != None and p.next != None:
            if p.next.val < p.val:
                temp = p.next
                p.next = p.next.next
                previous.next = temp
                temp.next = p
            else:
                p = p.next
            previous = previous.next
    return guard.next

def mergeSort(p):
    if p == None or p.next == None:
        return p
    mid = getMiddle(p)
    pr = mid.next
    mid.next = None
    pl = mergeSort(p)
    pr = mergeSort(pr)
    sortedList = merge(pl, pr)
    return sortedList

def merge(p1, p2):
    if p1 == None:
        return p2
    elif p2 == None:
        return p1
    guard = Node()
    if p1.val < p2.val:
        current = p1
        p1 = p1.next
    else:
        current = p2
        p2 = p2.next
    guard.next = current
    while p1 != None or p2 != None:
        if p1 == None:
            current.next = p2
            return guard.next
        if p2 == None:
            current.next = p1
            return guard.next
        if p1.val < p2.val:
            current.next = p1
            p1 = p1.next
        else:
            current.next = p2
            p2 = p2.next
        current = current.next
    return guard.next

def getMiddle(p):
    if p == None:
        return p
    slow = p
    fast = p
    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next
    return slow


def SortH(p,k):
    n = 0
    current = p
    while current != None:
        n += 1
        current = current.next
    if  n * k  <= 5000000:
        p = bubbleSort(p,k)
    else:
        p = mergeSort(p)
    print("Done")
    return p



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( SortH, all_tests = True )
