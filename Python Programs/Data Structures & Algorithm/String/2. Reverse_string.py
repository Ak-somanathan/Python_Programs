class Solution:
    # two pointers
    def reverseString(self, s):
        left = 0
        right = len(s) - 1
        chars = list(s)

        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

        return "".join(chars)

obj = Solution()

s = input()

print(obj.reverseString(s))