class Solution:
    # Hashing
    def commonElements1(self, arr1, arr2):
        seen = set(arr2)
        common = set()

        for i in arr1:
            if i in seen:
                common.add(i)
        
        return common

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

obj = Solution()

print(obj.commonElements1(arr1, arr2))
