class Solution:
    def isPerfect(self, n: int) -> bool:
        total = 0

        for i in range(1, n):
            if n%i == 0:
                total += i

        return 'true' if n == total else 'false'

obj = Solution()
n = int(input())
print(obj.isPerfect(n))