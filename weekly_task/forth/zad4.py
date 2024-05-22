from zad4testy import runtests
from math import abs


def is_in_range(a, b, t):
    if a > b:
        a, b = b, a
    return abs(a - b) <= 2 * t


def Flight(L, x, y, t):
    ans = False
    Q = []
    n = 0
    L.sort(key=lambda x: (x[0], x[1]))
    for e in L:
        n = max(n, e[1])
    min_height = [None] * n
    max_height = [None] * n
    if x > y:
        x, y = y, x
    for elem in L:
        if elem[0] == x:
            Q.append(elem)
    while len(Q) != 0 or i == len(L):
        current = Q[len(Q) - 1]
        Q.pop()
        if (
            current[1] == y
            and is_in_range(min_height[current[0]], current[1], t)
            or is_in_range(max_height[current[0]], current[1], t)
        ):
            return True
        if is_in_range():
    return ans


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(Flight, all_tests=True)
