class Solution:
    # sorting
    def lengthOfTheConsecutive1(self, arr):
        arr.sort()
        longest = 1
        current = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                continue

            elif arr[i] == arr[i - 1] + 1:
                current += 1
            
            else:
                current = 1

            longest = max(longest, current)

        return longest

    # hash set
    def lengthOfTheConsecutive2(self, arr):
        nums = set(arr)
        longest = 0

        for i in nums:
            if i - 1 not in nums:
                curr = i
                count = 1

                while curr + 1 in nums:
                    curr += 1
                    count += 1

                longest = max(longest, count)

        return longest
    
obj = Solution()

arr = list(map(int, input().split()))

print(obj.lengthOfTheConsecutive1(arr))
print(obj.lengthOfTheConsecutive2(arr))