class Solution:
    # two pointers
    def reverseWords1(self, s):
        l = s.split()
        left = 0
        right = len(l) - 1

        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

        return " ".join(l)

    # reverse method
    def reverseWords2(self, s):
        chars = s.split()
        chars.reverse()
        return " ".join(chars)

obj = Solution()

s = input()

print(obj.reverseWords1(s))

print(obj.reverseWords2(s))