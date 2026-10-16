class Solution:
    # two pointers
    def medianOfArrays1(self, arr1, arr2):
        n, m =len(arr1), len(arr2)
        prev = curr = 0
        i = j = 0

        for _ in range((n + m) // 2 + 1):
            prev = curr

            if i < n and (j >= m or arr1[i] < arr2[j]):
                curr = arr1[i]
                i += 1

            else:
                curr = arr2[j]
                j += 1

        if (n + m) % 2 == 1:
            print(curr)

        else:
            print((prev + curr) / 2)


    # binary search
    def medianOfArrays2(self, arr1, arr2):
        if len(arr1)> len(arr2):
            arr1, arr2 = arr2, arr1

        n, m = len(arr1), len(arr2)
        low, high = 0, n
        half = (n + m + 1) // 2

        while low <= high:
            i = (low + high) //2
            j = half - i

            left1 = arr1[i - 1] if i > 0 else float('-inf')
            right1 = arr1[i] if i < n else float('inf')
            left2 = arr2[j - 1] if j > 0 else float('-inf')
            right2 = arr2[j] if j < m else float('inf')

            if left1 <= right2 and left2 <= right1:
                if (n + m) % 2:
                    print(max(left1, left2))

                else:
                    print((max(left1, left2)+ min(right1, right2)) / 2)
                break 

            elif left1 > right2:
                high = i - 1

            else:
                low = i + 1

obj = Solution()

arr1 = list(map(int, input().split()))

arr2 = list(map(int, input().split()))

obj.medianOfArrays1(arr1, arr2)
obj.medianOfArrays2(arr1, arr2)