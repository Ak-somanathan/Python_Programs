class Solution:
    # sorted method
    def anagrams1(self, a, b):
        a = a.replace(" ", "").lower()
        b = b.replace(" ", "").lower()

        return sorted(a) == sorted(b)

    # Hash map
    def anagrams2(self, a, b):
        a = a.replace(" ", "").lower()
        b = b.replace(" ", "").lower()

        if len(a) != len(b):
            return False

        else:
            freq = {}

            for i in a:
                freq[i] = freq.get(i, 0) + 1

            for j in b:
                if j not in freq:
                    return False

                freq[j] -= 1

            else:
                return all(count == 0 for count in freq.values())

obj = Solution()

a,b = map(str, input().split())

print(obj.anagrams1(a, b))
print(obj.anagrams2(a, b))