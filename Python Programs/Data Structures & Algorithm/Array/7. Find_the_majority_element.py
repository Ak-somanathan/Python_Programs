# Hash map
def findMajorityElement1(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for num, count in freq.items():
        if count > (len(arr) // 2):
            return num
    return -1

# boyer's moore voting algorithm
def findMajorityElement2(arr):
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num

        if num == candidate:
            count += 1

        else:
            count -= 1
    return candidate

arr = list(map(int, input().split()))
print(findMajorityElement1(arr))
print(findMajorityElement2(arr))