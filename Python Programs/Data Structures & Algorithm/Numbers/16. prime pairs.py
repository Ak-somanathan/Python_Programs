class Solution:
    def prime_sum(self, n):
        def isPrime(num):
            if num < 2:
                return False

            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False

            return True

        for i in range(2, n//2+1):
            if isPrime(i) and isPrime(n-i):
                return True
        
        return False


obj = Solution()
n = int(input())
print(obj.prime_sum(n))