from collections import Counter

# sliding window + hashmap
def minimumWindowSubString(s, t):
    need = Counter(t)
    missing = len(t)
    best = len(s) + 1
    left = start = 0

    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1

        need[ch] -= 1

        while missing == 0:
            if right - left + 1 < best:
                best = right - left + 1
                start = left

            need[s[left]] += 1

            if need[s[left]] > 0:
                missing += 1

            left += 1

    return s[start : start + best] if best < len(s) else ""

s, t = map(str, input().split())

print(minimumWindowSubString(s, t))