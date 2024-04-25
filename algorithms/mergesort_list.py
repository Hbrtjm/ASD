class Node:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next


def merge(p1, p2):
    guard = Node()
    if p1.val > p2.val:
        guard.next = p1
        p1 = p1.next
    else:
        guard.next = p2
        p2 = p2.next
    current = guard.next
    while p2 != None or p1 != None:
        if p2 == None:
            current.next = p1
            current = current.next
            continue
        if p1 == None:
            current.next = p2
            current = current.next
            continue
        if p1.val > p2.val:
            current.next = p2.val
        else:
            current.next = p1.val
    return guard.next


def mergeSort(p, q):
    mid = getMiddle(p, q)
    l = mergeSort(p, mid)
    r = mergeSort(mid, q)
    return merge(r, l)


def getMiddle(p, q):
    if p == q:
        return p
    slow = p
    fast = p
    while fast.next != q and fast.next.next != q:
        fast = fast.next.next
        slow = slow.next
    return slow
