class Solution:
    # Sorting + Remove Duplicates
    def removeDuplicates1(self, nums: list[int]) -> int:
        nums = sorted(set(nums))
        return nums[-2]

    # Two pass linear scan
    def removeDuplicates2(self, nums: list[int]) -> int:
        largest = second = float('-inf')
        for i in nums:
            if i > largest:
                largest = i

        for i in nums:
            if i != largest and i>second:
                second = i

        return second

    # one pass linear scan
    def removeDuplicates3(self, nums: list[int]) -> int:
        largest = second = float('-inf')
        for x in nums:
            if x > largest:
                second = largest
                largest = x
            elif largest > x > second:
                second = x
        return second

obj = Solution()
print(obj.removeDuplicates1([1,35,35,0,9]))
print(obj.removeDuplicates2([1,35,25,0,9]))
print(obj.removeDuplicates3([1,35,2,34,0,9]))