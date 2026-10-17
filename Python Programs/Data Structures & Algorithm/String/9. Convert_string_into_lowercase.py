class Solution:
    # lower() method
    def convertToLowercase1(self, s):
        return s.lower()

    # without any built-ins
    def convertToLowercase2(self, s):
        res = []

        for i in s:
            if 'A' <= i <= 'Z':
                res += (chr(ord(i) + 32))
            else:
                res += i

        return "".join(res)

obj = Solution()

s = input()

print(obj.convertToLowercase1(s))

print(obj.convertToLowercase2(s))