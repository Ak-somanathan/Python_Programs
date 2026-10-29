from collections import Counter

def freqSort(s):
    freq = Counter(s)

    return "".join(i * count for i, count in freq.most_common())

s = input()
print(freqSort(s))