from zad3testy import runtests

def dominance(P):
  # tu prosze wpisac wlasna implementacje
  n = len(P)
  x = [ 0 ] * (n+1)
  y = [ 0 ] * (n+1)
  for ele in P:
    x[ele[0]]+=1
    y[ele[1]]+=1
  max_c = 0
  counter = 0
  x_pref = [ 0 ] * (n+1)
  y_pref = [ 0 ] * (n+1)
  for i in range(1,n):
    x_pref[i] += x_pref[i-1] + x[i]
    y_pref[i] = y_pref[i-1] + y[i]
  for ele in P:
    counter = x_pref[ele[0]-1] + y_pref[ele[1]-1] - n + 1
    max_c = max(counter,max_c)
  return max_c

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
