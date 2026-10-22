from collections import Counter

def findAnagrams(s, p):
    need = Counter(p)
    n = len(p)

    return [ i for i in range(len(s) - n + 1) if Counter(s[i : i + n]) == need]

s = input()

p = input()

print(findAnagrams(s, p))