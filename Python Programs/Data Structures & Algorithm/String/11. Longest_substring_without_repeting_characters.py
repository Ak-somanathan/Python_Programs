class Solution:
    # sliding window + hashset
    def longestSubString1(self, s):
        seen =set()
        longest = 0
        left = 0

        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[i])
                left += 1

            seen.add(s[i])
            longest = max(longest, i - left + 1)

        return longest

    # sliding window + hash map
    def longestSubString2(self, s):
        seen = {}
        longest = 0
        left = 0

        for i in range(len(s)):
            ch =s[i]

            if ch in seen and seen[ch] >= left:
                left = seen[ch] + 1

            seen[ch] = i
            longest = max(longest, i - left + 1)

        return longest 
                            
obj = Solution()

s = input()

print(obj.longestSubString1(s))
print(obj.longestSubString2(s))