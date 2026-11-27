class Solution:
    def leaders(self, nums):
        maxi = float('-inf')
        res = []

        for i in range(len(nums)-1, -1, -1):
            if nums[i] > maxi:
                res.append(nums[i])
                maxi = nums[i]
        
        return res[::-1]

obj = Solution()
nums = list(map(int, input().split()))
print(obj.leaders(nums))

        