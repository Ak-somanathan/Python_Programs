class Solution:
    # Single pass counting
    def stringCompression1(self, s):
        res = []
        count = 1

        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count += 1
                i += 1
            else:
                res.append(s[i-1] + str(count))
                count = 1

        res.append(s[-1] + str(count))
        compressed = "".join(res)
        return (compressed if len(compressed) < len(s) else s)

    # two pointers
    def stringCompression2(self, s):
        res =[]
        i = 0

        while i < len(s):
            count = 1

            while i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
                i += 1

            res.append(s[i] + str(count))
            i += 1

        compressed = "".join(res)
        return compressed if len(compressed) < len(s) else s

obj = Solution()

s = input()

print(obj.stringCompression1(s))
print(obj.stringCompression2(s))