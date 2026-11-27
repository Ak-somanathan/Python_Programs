class Solution:
    def isDivisibleBy9(self, s: str) -> bool:
        total = 0
        for i in s:
            total += int(i)
        return 'true' if total%9 == 0 else "false"

obj = Solution()
s = input()
print(obj.isDivisibleBy9(s))