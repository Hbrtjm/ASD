from collections import deque 
def bfs(G):
    visited = [ False ] * len(G)
    visited[0] = True
    Q = []
    Q.append(0)
    while len(Q)!=0:
        elem = Q.pop(0)
        for edge in G[elem]:
            if not visited[edge]:
                visited[edge] = True
                Q.append(edge)
                print(edge)


def dfs(G):
    visited = [False] * len(G)
    visited[0] = True
    Q = deque()
    Q.append(0)
    while Q:
        elem = Q.pop()
        for edge in G[elem]:
            if not visited[edge]:
                visited[edge] = True
                Q.append(edge)
                print(edge)

bfs([ [1, 6, 8],
  [0, 4, 6, 9],
  [4, 6],
  [4, 5, 8],
  [1, 2, 3, 5, 9],
  [3, 4],
  [0, 1, 2],
  [8, 9],
  [0, 3, 7],
  [1, 4, 7] ])
print("d")
dfs([ [1, 6, 8],
  [0, 4, 6, 9],
  [4, 6],
  [4, 5, 8],
  [1, 2, 3, 5, 9],
  [3, 4],
  [0, 1, 2],
  [8, 9],
  [0, 3, 7],
  [1, 4, 7] ])