from kol1btesty import runtests

def compare(word1,word2):
    for i in range(len(word2)):
        if word2[i] != word1[i]:
            return False
    return True

def f_optimal(T):
    # tu prosze wpisac wlasna implementacje
    T.sort(key=lambda word: len(word))
    U = [ [ 0 for _ in range(26) ] for _ in range(len(T)) ]
    for i in range(len(T)):
        for letter in T[i]:
            U[i][ord(letter)-ord('a')] += 1
    ans = 0
    temp = 1
    for i in range(len(T)-1):
        if compare(T[i],T[i+1]):
            temp += 1
        else:
            ans = max(ans,temp)
            temp = 1
    return ans

def f(T):
    anagram_counts = {}
    for word in T:
        table = [ 0 ] * 26
        for char in word:
            table[ord(char)-ord('a')] += 1
        key = tuple( elem for elem in table)
        if key in anagram_counts:
            anagram_counts[key] += 1
        else:
            anagram_counts[key] = 1

    return max(anagram_counts.values()) if anagram_counts else 0


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
