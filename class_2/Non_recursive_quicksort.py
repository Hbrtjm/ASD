# 1 QS zuzywajacy maks O(logn) pamieci na stosie
# zaimpl wstawianie do kocpa binarnego
# zaimpl QS bez rekurencji
# zaimpl merge dla k list
# zaproponuj strukture danych taka, ze ma insert, usuwanie min, usuwanie max - wszystkie O(logn)
# zaproponuj strukture danych taka, ze ma insert i usuwanie mediany
# zaimpl partition (qs) w wersji Hoare'a

class Node:
  def __init__(self, value=None):
    self.val = value
    self.next = None

def merge(t):
  k = len(t)
  res = ostatni = Node()
  wybrany = None

  def jeszcze(tab):
    n = len(tab)
    for i in range(n):
      if tab[i] is not None:
        return True
    return False

  while jeszcze(t):
    najm = float("inf")
    for i in range(k):
      if t[i] is None:
        continue

      if t[i].val <= najm:
        najm = t[i].val
        wybrany = t[i]
        nr_listy = i

    t[nr_listy] = t[nr_listy].next
    wybrany.next = None
    ostatni.next = wybrany
    ostatni = ostatni.next
  return res.next
