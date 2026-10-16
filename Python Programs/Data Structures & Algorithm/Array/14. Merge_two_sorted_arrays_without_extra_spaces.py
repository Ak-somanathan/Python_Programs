class Solution:
    # simple swapping + sorting
    def sortingArrays1(self, arr1, arr2):
        for i in range(len(arr1)):
            if arr1[i] > arr2[0]:
                arr1[i], arr2[0] = arr2[0], arr1[i]
                arr2.sort()
        return arr1, arr2

    # extra array + sort
    def sortingArrays2(self, arr1, arr2):
        arr = arr1 + arr2
        arr.sort()
        arr1[:] = arr[:len(arr1)]
        arr2[:] = arr[len(arr1):]
        return arr1, arr2

    # extra array + merge
    def sortingArrays3(self, arr1, arr2):
        arr = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                arr.append(arr1[i])
                i += 1
            else:
                arr.append(arr2[j])
                j += 1

        arr += arr1[i:]
        arr += arr2[j:]
        n = len(arr1)
        arr1[:] = arr[:n]
        arr2[:] = arr[n:]

        return arr1, arr2

    # Gap method - without extra spaces
    def sortingArrays4(self, arr1, arr2):
        n = m = len(arr1)
        gap = (n + m + 1) // 2
        while gap > 0:
            i = 0
            j = gap

            while j < n + m:
                if  i < n and j < m:
                    if arr1[i] > arr1[j]:
                        arr1[i], arr1[j] = arr1[j], arr1[i]

                elif i < n and j >= m:
                    if arr1[i] > arr2[j - n]:
                        arr1[i], arr2[j - n] = arr2[j - n], arr1[i]

                else:
                    if arr2[i -n] > arr2[j - n]:
                        arr2[i - n], arr2[j - n] = arr2[j - n], arr2[i-n]

                i += 1
                j += 1

            if gap == 1:
                gap = 0

            else:
                gap = (gap + 1) // 2

        return arr1, arr2


obj = Solution()

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

print(obj.sortingArrays1(arr1, arr2))
print(obj.sortingArrays2(arr1, arr2))
print(obj.sortingArrays3(arr1, arr2))
print(obj.sortingArrays4(arr1, arr2))
