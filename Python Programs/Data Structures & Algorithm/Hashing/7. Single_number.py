from typing import List

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res

nums = list(map(int, input("Enter the numbers separated by spaces: ").split()))

solution = Solution()
result = solution.singleNumber(nums)

print("Answer:", result)