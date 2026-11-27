class Solution:
    def isHarshad(self, n: int) -> bool:
        div = 0
        org = n

        while n > 0:
            div += n%10
            n = n // 10
        print(div)
        return "true" if org % div == 0 else "false"

obj = Solution()
n = int(input())
print(obj.isHarshad(n))