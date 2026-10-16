class Solution:
    # string + set
    def numbersNoDigits1(self, n1, n2):
        count = 0

        for i in range(n1, n2+1):
            digit = str(i)

            if len(digit) == len(set(digit)):
                count += 1

        return count

    # digit extraction + bitmask
    def numbersNoDigits2(self, n1, n2):
        count = 0

        for i in range(n1, n2 + 1):
            temp = i
            seen = set()

            while temp > 0:
                digit = temp % 10

                if digit in seen:
                    break

                seen.add(digit)
                temp //= 10

            else:
                count += 1

        return count

obj = Solution()

n1 = int(input())
n2 = int(input())

print(obj.numbersNoDigits1(n1, n2))
print(obj.numbersNoDigits2(n1, n2))