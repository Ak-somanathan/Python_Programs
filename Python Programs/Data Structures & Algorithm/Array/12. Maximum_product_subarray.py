class Solution:
    # prefix / suffix product pattern
    def productSubArray1(self, arr):
        prefix = 1
        suffix = 1
        maximum = arr[0]
        n = len(arr)

        for i in range(n):
            prefix *= arr[i]
            suffix *= arr[n - 1 - i]
            maximum = max(prefix, suffix, maximum)

            if prefix == 0:
                prefix = 1

            if suffix == 0:
                suffix = 1

        return maximum

    # track max and min 
    def productSubArray2(self, arr):
        maximum = arr[0]
        minimum = arr[0]
        ans = arr[0]

        for num in arr[1:]:
            if num < 0:
                maximum, minimum = minimum, maximum
            maximum = max(num, maximum * num)
            minimum = min(num, minimum * num)
            ans = max(ans, maximum)

        return ans

    # without built-in methods
    def productSubArray3(self, arr):
        maximum = arr[0]
        minimum =arr[0]
        ans = arr[0]

        max_start = 0
        min_start = 0
        best_start = 0
        best_end = 0

        for i in range(1, len(arr)):
            num = arr[i]

            if num < 0:
                maximum, minimum = minimum, maximum
                max_start, min_start = min_start, max_start

            if num > maximum * num:
                maximum = num
                max_start = i

            else:
                maximum = maximum * num

            if num < minimum * num:
                minimum = num
                min_start = i
            else:
                minimum = minimum * num

            if maximum >= ans:
                ans = maximum
                best_start = max_start
                best_end = i

        return arr[best_start : best_end + 1]

obj = Solution()
arr = list(map(int, input().split()))
print(obj.productSubArray1(arr))
print(obj.productSubArray2(arr))
print(obj.productSubArray3(arr))
