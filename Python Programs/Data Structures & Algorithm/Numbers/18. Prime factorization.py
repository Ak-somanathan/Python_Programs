class Solution:
    def primeFactorization(self, queries):
        res = []

        for num in queries:
            factors = []
            i = 2

            while i * i <= num:
                while num % i == 0:
                    factors.append(i)
                    num //= i
                
                i += 1

            if num > 1:
                factors.append(num)

            res.append(factors)

        return res

obj = Solution()

queries = list(map(int,input().split()))

print(obj.primeFactorization(queries))        