class Solution:
    # linear search + sort
    def missingNumber1(self, nums: list[int], n: int) -> int:
        nums.sort()
        for i in range(1,n+1):
            if i not in nums:
                return i

    # sorting
    def missingNumber2(self, nums: list[int], n: int) -> int:
        nums.sort()
        for i in range(n-1):
            if nums[i] != i+1:
                return(i+1)
        else:
            return n

    # sum formula
    def missingNumber3(self, nums: list[int], n:int) -> int:
        expected_sum = n * (n+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

    # Xor
    def missingNumber4(self, nums: list[int], n: int) -> int:
        xor = n
        for i in range(n-1):
            xor ^= (i+1) ^ nums[i]
        return xor

obj = Solution()
print(obj.missingNumber1([1,3,4,5], 5))
print(obj.missingNumber2([3,2,4], 4))
print(obj.missingNumber3([1,2,3,4,5], 6))
print(obj.missingNumber4([1,2,3,5], 5))