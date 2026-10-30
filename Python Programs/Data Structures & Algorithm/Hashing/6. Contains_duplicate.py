from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

nums = list(map(int, input("Enter the numbers separated by spaces: ").split()))

solution = Solution()
result = solution.containsDuplicate(nums)

print("Answer:", result)