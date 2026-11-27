class Solution:
    def decimalToBinary(self, n):
        if n == 0:
            return "0"

        res = ""

        while n > 0:
            rem = n % 2
            res += str(rem)
            n //= 2

        return res[::-1]

obj = Solution()

n = int(input())

print(obj.decimalToBinary(n))