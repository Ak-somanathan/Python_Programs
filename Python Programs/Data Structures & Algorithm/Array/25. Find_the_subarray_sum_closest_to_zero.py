arr = [1, -2, 4, -5, 6]

prefix = [(0, 0)]
total = 0

for i, num in enumerate(arr):
    total += num
    prefix.append((total, i + 1))

prefix.sort()

closest = None

for i in range(1, len(prefix)):
    sum1, index1 = prefix[i - 1]
    sum2, index2 = prefix[i]

    if index1 < index2:
        sub_sum = sum2 - sum1
    else:
        sub_sum = sum1 - sum2

    if closest is None or abs(sub_sum) < abs(closest):
        closest = sub_sum

print(closest)