def findMinimum(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[right] > arr[right]:
            left = mid + 1

        else:
            right = mid

    return arr[left]

arr = list(map(int, input().split()))

print(findMinimum(arr))