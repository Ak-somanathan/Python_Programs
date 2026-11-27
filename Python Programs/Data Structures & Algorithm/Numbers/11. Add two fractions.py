class Solution:
    def addFractions(self, frac1: str, frac2: str) -> str:
        a, b = map(int, frac1.split('/'))
        c, d = map(int, frac2.split('/'))
        num = (a * d) + (c * b)
        deno = b * d

        x, y = num, deno

        while y:
            x, y = y, x % y

        gcd = x
        num //= gcd
        deno //= gcd

        return f'{num}/{deno}'

obj = Solution()

frac1 = input()
frac2 = input()

print(obj.addFractions(frac1, frac2))