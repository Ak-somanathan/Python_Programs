def firstNonRepetingCharacter(s):
    freq = {}

    for i in s:
        freq[i] = freq.get(i, 0) + 1

    for ch in freq.keys():
        if freq[ch] == 1:
            return ch

    return "#"

s = input()
print(firstNonRepetingCharacter(s))