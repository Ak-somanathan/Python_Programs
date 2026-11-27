class Solution:
    def lcm(self, n1: int, n2: int) -> int:
        if n1 == 0 or n2 == 0:
            return 0

        a, b = n1, n2

        while b != 0:
            a, b = b, a % b

        return abs((n1 * n2) // a)


obj = Solution()
n1, n2 = map(int, input().split())
print(obj.lcm(n1, n2))