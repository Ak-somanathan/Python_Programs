class Solution:
    def intersectionArray(self, nums1, nums2):
        i = 0
        j = 0
        res =[]

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1

            elif nums1[i] < nums2[j]:
                i += 1

            else:
                j += 1

        return res

obj = Solution()

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

print(obj.intersectionArray(nums1, nums2))