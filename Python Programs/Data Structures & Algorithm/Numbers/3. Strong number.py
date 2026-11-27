class Solution:
    def isStrongNumber(self, n):
        org = n
        total = 0

        while n > 0:
            digit = n % 10

            fact = 1 
            for i in range(1, digit + 1):
                fact *= i
            total += fact

            n = n // 10
        
        return "Yes" if total == org else "No"
        
obj = Solution()

n = int(input())

print (obj.isStrongNumber(n))