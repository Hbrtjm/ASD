from zad4testy import runtests

def Flight(L,x,y,t):
  ans = False
  max_vertice = 0
  # tu prosze wpisac wlasna implementacje
  for elem in L:
    max_vertice = max(max_vertice,elem)
  if x > y:
    x, y = y, x
  connection_vector = [ [] for _ in range(max_vertice)]
  for elem in L:
    connection_vector[elem[0]].append(elem[1])
    connection_vector[elem[1]].append(elem[0])
  
  return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )
