class Solution:
    def minimumBitFlips(self, start, goal):
        count = 0
        num = start ^ goal

        while num > 0:
            count += num % 2
            num //= 2
        
        return count

obj = Solution()

start, goal = map(int, input().split())

print(obj.minimumBitFlips(start, goal))