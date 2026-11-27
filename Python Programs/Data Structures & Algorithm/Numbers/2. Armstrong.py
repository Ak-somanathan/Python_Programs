class Solution:
    def isArmstrong(self, n):
        org = n
        total = 0
        length = len(str(n))

        while n > 0:
            digit = n % 10
            total += digit ** length
            n = n // 10

        return total == org

obj = Solution()

n = int(input())

print (obj.isArmstrong(n))