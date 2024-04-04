def parent(i):
   return (i - 1)//2

def heap_insert(t, val):
  n = len(t)
  t.append(val)
  i = n
  p = parent(i)
  while i > 0 and t[p] < t[i]:
      t[p], t[i] = t[i], t[p]
      i = p
      p = parent(i)

