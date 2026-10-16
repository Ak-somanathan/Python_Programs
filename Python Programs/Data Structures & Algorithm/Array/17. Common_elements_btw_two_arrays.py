class Solution:
    # Hashing
    def commonElements1(self, arr1, arr2):
        seen = set(arr2)
        common = []

        for i in arr1:
            if i in seen and i not in common:
                common.append(i)
        
        return common

    # set intersection
    def commonElements2(self, arr1, arr2):
        return list(set(arr1) & set(arr2))

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

obj = Solution()

print(obj.commonElements1(arr1, arr2))
print(obj.commonElements2(arr1, arr2))
