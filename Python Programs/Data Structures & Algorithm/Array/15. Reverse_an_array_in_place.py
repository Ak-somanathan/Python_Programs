class Solution:
    # two pointers
    def reverseArray1(self, arr):
        left = 0
        right = len(arr) - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return arr

    # reverse traversal
    def reverseArray2(self, arr):
        res = []
        for i in range(len(arr)-1, -1, -1):
            res.append(arr[i])

        return res

    # slicing
    def reverseArray3(self, arr):
        return arr[::-1]

    # built-in method
    def reverseArray4(self, arr):
        arr.reverse()

        return arr

arr = list(map(int, input().split()))

obj = Solution()

print(obj.reverseArray1(arr))