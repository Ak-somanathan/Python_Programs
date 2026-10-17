class Solution:
    # two pointers
    def palindromCheck(self, s):
        left = 0
        right = len(s) - 1
        is_palindrome = True

        while left < right:
            if not s[left].isalnum():
                left += 1
                s[left]

            elif not s[right].isalnum():
                right -= 1

            elif s[left].lower() != s[right].lower():
                is_palindrome = False
                break

            else:
                left += 1
                right -= 1

        return is_palindrome

obj = Solution()

s = input()

print(obj.palindromCheck(s))