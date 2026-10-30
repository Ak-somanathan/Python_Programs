def searchRange(arr, target):
    def binarySearch(findFirst):
        left, right = 0, len(arr) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                result = mid

                if findFirst:
                    right = mid - 1

                else:
                    left = mid + 1

            elif arr[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return result

    return [binarySearch(True), binarySearch(False)]

arr = list(map(int, input().split()))

target = int(input())

print(searchRange(arr, target))