class Solution:
    # List comprehension
    def rearrangeMultiples1(self, arr):
        arr = [x for x in arr if x % 10 != 0] + [x for x in arr if x % 10 == 0]

        return arr

    # two pointers
    def rearrangeMultiples2(self, arr):
        left = 0

        for right in range(len(arr)):
            if arr[right] % 10 != 0:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1

        return arr

obj = Solution()

arr = list(map(int, input().split()))

print(obj.rearrangeMultiples1(arr))
print(obj.rearrangeMultiples2(arr))