from random import randint

class Node:
  def __init__(self, val = None, next = None):
      self.val = val
      self.next = next

def merge_k_linkedList(T):
  ret = Node(None)
  p = ret

  while len(T) > 1:

      mini = (0, float('inf'))
      i = 0

      while i < len(T):

          if(T[i] == None):
              T.pop(i)
              continue

          if(T[i].val < mini[1]):
              mini = (i, T[i].val)

          i += 1

      p.next = T[mini[0]]
      p = p.next
      T[mini[0]] = T[mini[0]].next

  p.next = T[0]

  return ret.next

def gen_array(lenght, start = 0, stop = 1000):
  result = []
  for i in range(lenght):
      result.append(randint(start, stop))

  return result

def print_list(p):
  wynik = ""
  while p != None:
      wynik += str(p.val) + " -> "
      p = p.next

  print(wynik + "NONE")

def gen_list(t):
  t = t[::-1]
  n1 = None
  n2 = Node(t[0], n1)
  for i in t[1:]:
      n1 = n2
      n2 = Node(i, n1)

  return n2


array = []
for i in range(5):
    t = gen_array(10+2*i)
    t.sort()
    array.append(gen_list(t))

for i in range(5):
    print_list(array[i])

print_list(merge_k_linkedList(array))