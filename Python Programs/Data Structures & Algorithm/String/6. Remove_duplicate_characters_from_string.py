class Solution:
    # Hash set
    def removeDuplicates1(self, s):
        seen = set()
        res = []

        for i in s:
            if i not in seen:
                seen.add(i)
                res.append(i)

        return "".join(res)

obj = Solution()

s= input()

print(obj.removeDuplicates1(s))

