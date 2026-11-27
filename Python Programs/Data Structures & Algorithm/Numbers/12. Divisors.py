class Solution:
    def divisors(self, n):
        res =[]
        for i in range(1, int(n ** 0.5) + 1):
            if n%i == 0:
                res.append(i)

                if i != n // i:
                    res.append(n // i)
        
        return sorted(res)

obj = Solution()
n = int(input())
print(obj.divisors(n))