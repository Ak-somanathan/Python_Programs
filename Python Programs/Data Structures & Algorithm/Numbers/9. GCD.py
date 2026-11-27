class Solution:
    def GCD(self, n1, n2):
        while n2 != 0:
            n1, n2 = n2, n1%n2

        return n1

obj = Solution()
n1, n2 = map(int, input().split())
print(obj.GCD(n1, n2))
    