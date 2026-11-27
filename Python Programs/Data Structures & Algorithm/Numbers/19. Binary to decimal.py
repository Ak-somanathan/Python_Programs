class Solution:
    def binaryToDecimal(self, n):
        res = 0

        for i in str(n):
            res = res * 2 + int(i)

        return res

obj = Solution()

n = input()

print(obj.binaryToDecimal(n))