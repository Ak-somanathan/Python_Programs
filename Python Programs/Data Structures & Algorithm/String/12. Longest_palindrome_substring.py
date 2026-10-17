class Solution:
    # Expand around center
    def longestPalindrome(self, s):
        start = 0
        max_len = 0

        # odd length palindrome
        for i in range(len(s)):
            left = right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    start = left
                    max_len = right - left + 1

                left -= 1
                right += 1

        # Even length palindrome
        for i in range(len(s)):
            left, right = i, i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    start = left
                    max_len = right - left+ 1

                left -= 1
                right += 1

        return s[start : start + max_len]

obj = Solution()

s = input()

print(obj.longestPalindrome(s))