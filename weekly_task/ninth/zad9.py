from zad9testy import runtests

def is_valid(x,y,n,m):
  return m > x >= 0 and n > y >= 0

def trip(M):
  answer = 0
  m = len(M)
  n = len(M[0])
  dp = [ [ 0 for _ in range(n) ] for _ in range(m) ]
  # coordinates = [ None for _ in range(m*n) ]
  alternative = [  ]
  for i in range(m):
    for j in range(n):
      alternative.append((M[i][j],i,j))
      # coordinates[M[i][j]-1] = (i,j)
  alternative = sorted(alternative,key=lambda x: x[0])
  # coordinates = coordinates[::-1]
  # print(coordinates)
  visited = [ [ False for _ in range(n) ] for _ in range(m) ]
  moves = [ [0,1] , [1,0] , [-1,0] , [0,-1] ]
  for d, i, j in alternative:
      if not visited[i][j]:
        stack = [(i,j)]
        dp[i][j] = 1
        while len(stack) != 0:
          x, y = stack.pop(0)
          visited[x][y] = True
          for dx,dy in moves:
            new_x , new_y = x+dx, y+dy
            if is_valid(new_x,new_y,n,m):
              if M[new_x][new_y] > M[x][y]:
                if dp[x][y] + 1 > dp[new_x][new_y]:
                  dp[new_x][new_y] = dp[x][y] + 1
                  answer = max(dp[new_x][new_y],answer)
                  stack.append((new_x,new_y))
  return answer

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = True )
