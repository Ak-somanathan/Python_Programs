def quickSort(arr, low, high):
    if low < high:
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        p = i + 1

        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)

    return arr

arr = list(map(int, input().split()))

print(quickSort(arr, 0, len(arr)-1))