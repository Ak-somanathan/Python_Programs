class Solution:
    def permutations(self, n, r):
        if r > n:
            return 0

        mod = 10 ** 9 + 7
        res = 1

        for i in range(n - r + 1, n+1):
            res = (res * i) % mod

        return res

obj = Solution()
n, r = map(int, input().split())
print(obj.permutations(n, r))