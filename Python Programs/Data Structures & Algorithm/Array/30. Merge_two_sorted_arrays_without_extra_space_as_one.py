class Solution:
    # Gap method - without extra spaces
    def sortingArrays(self, arr1, arr2):
        n = len(arr2)
        m = len(arr1) - n

        gap = (n + m + 1) // 2

        while gap > 0:
            i = 0
            j = gap

            while j < n + m:
                if i < m and j < m: 
                    if arr1[i] > arr1[j]:
                        arr1[i], arr1[j] = arr1[j], arr1[i]

                elif i < m and j >= m:
                    if arr1[i] > arr2[j - m]:
                        arr1[i], arr2[j - m] = arr2[j - m], arr1[i]

                else:
                    if arr2[i - m] >arr2[j - m]:
                        arr2[i - m], arr2[j -m]= arr2[j-m], arr2[i-m]

                i += 1
                j += 1

            if gap == 1:
                gap = 0

            else:
                gap = ( gap + 1 ) //2

        for i in range(n):
            arr1[m+i] = arr2[i]

        return arr1


obj = Solution()

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

print(obj.sortingArrays(arr1, arr2))