class Solution:
    # prefix sum + Hashmap
    def subArraySum1(self, arr, target):
        prefix_sum = 0
        seen = {0:[-1]}

        for i, num in enumerate(arr):
            prefix_sum += num
            need = prefix_sum - target

            if need in seen:
                for j in seen[need]:
                    print(arr[j+1 : i+1])

            seen.setdefault(prefix_sum, []).append(i)

    # sliding window
    def subArraySum2(self, arr, target):
        left = 0
        total = 0

        for right in range(len(arr)):
            total += arr[right]

            while total > target and left <= right:
                total -= arr[left]
                left += 1

            if total == target:
                print(arr[left : right + 1])

obj = Solution()

arr = list(map(int,input().split()))
target = int(input())
obj.subArraySum1(arr, target)
obj.subArraySum2(arr, target)