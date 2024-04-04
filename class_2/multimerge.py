
class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None

def merge(t1,t2):
    guard = Node()
    if t1 == None:
        return t2
    if t2 == None:
        return t1
    if t1.val > t2.val:
        guard.next = t1
    if t2.val > t1.val:
        guard.next = t2
    current = guard.next
    while t1 != None or t2 != None:
        if t1 == None:
            current.next = t2
            return guard.next
        if t2 == None:
            current.next = t1
            return guard.next
        if t1.val > t2.val:
            current.next = t2
            t2 = t2.next
        else:
            current.next = t1
            t1 = t1.next
        current = current.next
    return guard.next

def multimerge(T):
    def rekmerge(left,right):
        if len(left) <= 1 and len(right) <= 1:
            return merge(left[0],right[0])
        return merge(rekmerge(left[len(left)//2:],left[:len(left)//2]),rekmerge(right[len(right)//2:],right[:len(right)//2]))
        
        
    return rekmerge(T[len(T)//2:],T[:len(T)//2])