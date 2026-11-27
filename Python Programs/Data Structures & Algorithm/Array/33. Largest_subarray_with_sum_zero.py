class Solution:
    def subArraySum(self, arr):
        prefix_sum = 0
        seen = {0: -1}
        longest = 0

        for i, num in enumerate(arr):
            prefix_sum += num

            if prefix_sum in seen:
                longest = max(longest, i - seen[prefix_sum])
            else:
                seen[prefix_sum] = i

        return longest
obj = Solution()
arr = list(map(int, input().split()))
print(obj.subArraySum(arr))