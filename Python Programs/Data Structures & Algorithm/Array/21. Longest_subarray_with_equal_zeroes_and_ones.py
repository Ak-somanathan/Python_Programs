class Solution:
    # prefix_sum + hashmap
    def longestSubArray(self, arr):
        prefix_sum = 0
        seen = {0 : -1}
        longest = 0

        for i, num in enumerate(arr):
            if num == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            if prefix_sum in seen:
                longest = max(longest , i - seen[prefix_sum])

            else:
                seen[prefix_sum] = i

        return longest

obj = Solution()

arr = list(map(int, input().split()))

print(obj.longestSubArray(arr))