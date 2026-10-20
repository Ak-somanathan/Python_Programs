from collections import Counter

def uniqueCharacter(s):
    freq = Counter(s)

    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i, s[i]

s = input()

print(uniqueCharacter(s))