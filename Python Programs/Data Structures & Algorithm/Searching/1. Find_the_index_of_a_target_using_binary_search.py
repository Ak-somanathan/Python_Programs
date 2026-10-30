def binarySearch(arr, target):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left += 1

        else:
            right -= 1

    return mid

arr = list(map(int, input().split()))

target = int(input())

print(binarySearch(arr, target))