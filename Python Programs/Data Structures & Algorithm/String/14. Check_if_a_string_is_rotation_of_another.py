class Solution:
    # string doubling
    def rotationOfAnother1(self, s1, s2):
        return (len(s1) == len(s2) and s2 in s1 + s1)

    # brute force
    def rotationOfAnother2(self, s1, s2):
        if len(s1) == len(s2):
            for i in range(len(s1)):
                if s1[i:] + s1[:i] == s2:
                    return True
            else:
                return False

obj = Solution()

s1, s2 = map(str, input().split())

print(obj.rotationOfAnother1(s1, s2))

print(obj.rotationOfAnother2(s1, s2))