from egzP1atesty import runtests 

def find_morse(c,M):
    sorted(M,key=lambda x: x[0])
    n = len(M)
    l = 0 
    r = n-1
    while l <= r:
        mid = (l + r)//2
        if ord(c) < ord(M[mid][0]):
            r = mid - 1
        elif  ord(c) > ord(M[mid][0]):
            l = mid + 1
        else:
            return M[mid][1]
    return None

class Node:
    def __init__(self,val = ""):
        self.val = val
        self.left = None
        self.right = None

def insert_into_tree(bst,available):
    guard = bst

    for char in available:
        if char == ".":
            if bst.left == None:
                bst.left = Node(available)
                break
            bst = bst.left
        else:
            if bst.right == None:
                bst.right = Node(available)
                break
            bst = bst.right
    return guard

def find_on_tree(bst,x):
    current = bst
    for char in x:
        if current.val == x:
            return True
        if char == ".":
            if current.left == None:
                break
            current = current.left
        else:
            if current.right == None:
                break
            current = current.right
    return x == current.val

def titanic( W, M, D ):
    string = ""
    bst = Node()
    bst.left = Node(".")
    bst.right = Node("-")
    available_table = [ find_morse(chr(c+ord('A')),M) for c in D ]
    print(available_table)
    available_table = sorted(available_table,key=lambda x:len(x))
    for available in available_table:
        bst = insert_into_tree(bst,available)
    for char in W:
        string = string + find_morse(char,M)
    n = len(string)
    dp = [ [ float('inf') for _ in range(4) ] for _ in range(n) ]
    dp[0][0] = 1
    ans = [ float('inf') for _ in range(n) ]
    ans[0] = 1
    for i in range(1,n):
        current_string = ""
        for j in range(4):
            if i - j < 0:
                break
            current_string = string[i-j] + current_string
            if find_on_tree(bst,current_string):
                if i - j - 1 >= 0:
                    dp[i][j] = ans[i-j-1]+1
                else:
                    dp[i][j] = 1
        for j in range(4):
            if n < 20:
                print(dp[i])
            ans[i] = min(dp[i][j],ans[i])
    return ans[n-1]

runtests ( titanic, recursion=False )