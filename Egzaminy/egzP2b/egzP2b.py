from egzP2btesty import runtests
from math import log10

class Node:
    def __init__(self):
        self.value = None
        self.leaves = 1
        self.fresh = True
        self.exists = False
        self.left = None
        self.right = None

def print_tree(bst):
    if bst == None:
        print("None")
        return
    print(bst.value,end = " ")
    print("LEFT", end="")
    print_tree(bst.left)
    print("RIGHT",end="")
    print_tree(bst.right)

def create_tree(string,bst):
    guard = bst
    n = len(string)
    # current_string = ""
    for i in range(n-1,-1,-1):
        if string[i] == '0':
            # current_string = '0' + current_string
            if bst.left == None:
                bst.left = Node()
            # Tu jest problem, jak po prostu dodaję to dla tych, które nie istnieją (jak 11)
            # doliczamy liść, ale tutaj po prostu przechodzimy niżej, a 11 nie istnieje dla nas
            # istnieje tylko 1111
            bst.leaves = bst.leaves + 1
            bst = bst.left
            # bst.value = current_string
        else:
            # current_string = '1' + current_string
            if bst.right == None:
                bst.right = Node()
            bst.leaves = bst.leaves + 1
            bst = bst.right
            # bst.value = current_string
    bst.exists = True
    return guard

def find_on_tree(string,bst):
    current = bst
    n = len(string)
    for i in range(n-1,-1,-1):
        if string[i] == '0':
            current = current.left
        else:
            current = current.right
    # print(f"{current.value} {current.leaves}")
    # print_tree(current)
    # Trzeba było po prostu wywalić te, które nie "istnieją", więc liczyć tylko 
    # liście w ich poddrzewie znajdują się w tablicy
    if current.exists:
        return current.leaves
    return current.leaves - 1

def kryptograf( D, Q ):    
    ans = 0
    bst = Node()
    bst.exists = True
    bst.leaves = 0
    for string in D:
        bst = create_tree(string,bst)
    for string in Q:
        # Zamiast mnożenia skorzystać z własnoci logarytmu
        # ans *= find_on_tree(string,bst) # Dobra, idk czemu to jest log(n)
        ans += log10(find_on_tree(string,bst)) # Optymalna
    # print(ans)
    return ans
    # return log10(ans)

# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
runtests(kryptograf, all_tests = 3)