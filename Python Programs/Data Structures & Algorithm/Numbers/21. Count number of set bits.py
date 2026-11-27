class Solution:
    def numberOfSetBits(self, n):
        res = 0

        while n > 0:
            res += n % 2
            n //= 2

        return res

obj = Solution()

n = int(input())

print(obj.numberOfSetBits(n))