from kol1atesty import runtests

def gi(T):
    # tu prosze wpisac wlasna implementacje
    U = [ 0 ] * len(T)
    for i in range(len(T)):
        for letter in T[i]:
            U[i] += 2 ** (ord(letter) - ord('a'))
    U.sort()
    ans = 0
    temp = 1
    for i in range(len(T)-1):
        if U[i] == U[i+1]:
            temp += 1
        else:
            ans = max(ans,temp)
            temp = 1
    return ans

def g(T):
    anagram_counts = {}
    for word in T:
        key = word[::-1] if word[::-1] in anagram_counts else word
        if key in anagram_counts:
            anagram_counts[key] += 1
        else:
            anagram_counts[key] = 1
    print(anagram_counts)
    return max(anagram_counts.values()) if anagram_counts else 0


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )
