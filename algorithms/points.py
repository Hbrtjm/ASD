def place(elem, R, n):
    return int((elem[0] ** 2 + elem[1]) / R**2 * n)


def points(A, R, k=10):
    n = len(A)
    C = [0] * k
    B = [0] * n
    for x in A:
        C[place(x, R, n)] += 1
    for i in range(1, k):
        C[i] += C[i - 1]
    for x in A:
        placement = place(x, R, n)
        B[C[placement] - 1] = x
        C[placement] -= 1
    for i in range(n):
        B[i] = A[i]


def solve(A):
    R = 10
    print(points(A, R, len(A)))
