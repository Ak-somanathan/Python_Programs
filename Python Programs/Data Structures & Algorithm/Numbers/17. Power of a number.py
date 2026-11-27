class Solution:
    def power(self, base, p):

        mod = 10 ** 9 + 7
        res = 1
        base = base % mod

        while p > 0:
            if p % 2 == 1:
                res = (res * base) % mod

            base = (base * base) % mod
            p = p // 2

        return res

obj = Solution()
base, p = map(int, input().split())
print(obj.power(base, p))