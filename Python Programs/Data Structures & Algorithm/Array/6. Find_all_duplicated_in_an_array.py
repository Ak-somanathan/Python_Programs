# Hash set
def findDuplicates1(arr):

    for num in arr:
        if num in seen:
            if num not in duplicates:
                duplicates.append(num)
        else:
            seen.add(num)
    return duplicates

# in-place using indices
def findDuplicates2(arr):
    for num in arr:
        index = abs(num) - 1

        if arr[index] < 0:
            if abs(num) not in duplicates:
                duplicates.append(abs(num))

        else:
            arr[index] = -arr[index]

    return duplicates

arr = list(map(int,input().split()))
duplicates = []
seen = set()

print(findDuplicates1(arr))
print(findDuplicates2(arr))