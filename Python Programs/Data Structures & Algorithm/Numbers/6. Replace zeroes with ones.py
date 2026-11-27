class Solution:
    def replaceZerosWithOnes(self, n: int) -> int:
        if n == 0:
            return 1
        
        res = 0
        place = 1

        while n > 0:
            digit = n % 10

            if digit == 0:
                digit = 1
            
            res += digit * place
            place *= 10
            n = n // 10
        
        return res

obj = Solution()
n = int(input())
print(obj.replaceZerosWithOnes(n))