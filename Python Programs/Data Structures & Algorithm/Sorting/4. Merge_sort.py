def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    res = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1

        else:
            res.append(right[j])
            j += 1

    return res + left[i:] + right[j:]

arr = list(map(int, input().split()))

print(mergeSort(arr))