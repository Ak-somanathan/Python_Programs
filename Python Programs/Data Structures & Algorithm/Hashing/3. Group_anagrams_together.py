def groupAnagrams(s):
    groups={}

    for i in s:
        key = ''.join(sorted(i))

        if key not in groups:
            groups[key] = []

        groups[key].append(i)

    return list(groups.values())

s = list(map(str, input().split()))

print(groupAnagrams(s))