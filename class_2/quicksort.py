def qs(tab, p, k):
    j = partition(tab, p, k)
    qs(tab, p, j-1)
    qs(tab, j, k)
    
def quicksort(tab, p, k):
    while p < k:
        i = partition(tab, p, k)
        if i - 1 - p > k - i:
            quicksort(tab, i+1, k)
            k = i - 1
        else:
            quicksort(tab, p, i-1)
            p = i+1
    return tab


def partition(A,p,r):
  #pivot = randint(p,r)
  #A[r],A[pivot]=A[pivot],A[r]
  i = p - 1
  for j in range(p,r):
      if A[j]<=A[r]:
          i+=1
          A[j],A[i]=A[i],A[j]
  A[i+1],A[r]=A[r],A[i+1]
  return i+1

from random import randint
import time
import matplotlib.pyplot as mp

N = 10000

times = []
place = []

for o in range(N):
    T = [ randint(1,2**24) for i in range(N) ]
    start = time.perf_counter()
    T = quicksort(T,0,N-1)
    # print(T)
    stop = time.perf_counter()
    deltatime = stop-start
    # print(deltatime)
    place.append(o)
    times.append(deltatime)
mp.plot(place,times)
mp.show()