class Solution:
    # Hash map
    def countOccurences1(self, s):
        freq = {}

        for i in s:
            freq[i] = freq.get(i, 0) + 1

        for i, count in freq.items():
            print(f'{i}: {count}', end = ", ")


obj = Solution()

s = input()

obj.countOccurences1(s)