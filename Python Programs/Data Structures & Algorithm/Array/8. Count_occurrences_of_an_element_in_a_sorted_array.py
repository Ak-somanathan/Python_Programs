import bisect

class Solution1:
    # shortcut method
    def countOccurrences1(self, arr, target):
        return arr.count(target)

    # linear search
    def countOccurrences2(self, arr, target):
        count = 0
        for i in arr:
            if i == target:
                count += 1
        return count


class Solution2:
    # binary search
    def find_position1(self, first):
        left = 0
        right = len(arr) - 1
        position = -1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                position = mid
                if first:
                    right = mid - 1
                else:
                    left = mid + 1

            elif arr[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return position

    # python's bisect
    def find_position2(self, arr, target):
        first = bisect.bisect_left(arr, target)
        last = bisect.bisect_right(arr, target)

        return last - first


arr = list(map(int, input().split()))
target = int(input())

obj1 = Solution1()
print(obj1.countOccurrences1(arr, target))
print(obj1.countOccurrences2(arr, target))

obj2 = Solution2()
first = obj2.find_position1(True)
last = obj2.find_position1(False)

if first == -1:
    print(0)
else:
    print(last - first + 1)

print(obj2.find_position2(arr, target))