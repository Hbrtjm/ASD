def radix(A, k=10):
    n = len(A)
    maximal = 0
    B = [None] * n
    for elem in range(len(A)):
        maximal = max(maximal, elem)
    for current_letter in range(maximal - 1, -1, -1):
        C = [0] * k
        for x in A:
            C[x[current_letter]] += 1
        for i in range(1, k):
            C[i] += C[i - 1]
        for i in range(n - 1, -1, -1):
            B[C[A[i]] - 1] = A[i]
            C[A[i]] -= 1
        for i in range(n):
            A[i] = B[i]


def count_single(n):
    a = [0] * 10
    while n > 0:
        a[n % 10] += 1
        n //= 10
    s = 0
    b = 0
    for i in a:
        if i == 1:
            s += 1
        if i > 1:
            b += 1
    return (s, b)


def solve(T):
    A = [ count_single(elem) for elem in T ]
    radix(A, 2)
    return A
