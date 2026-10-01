class Solution:
    # Two pointer - swap
    def addZeroes(self, nums: list[int]) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j+=1
        return nums

obj = Solution()
print(obj.addZeroes([1,0,35,0,9]))
