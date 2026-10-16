import heapq

class Solution:
    # sorting
    def kthLargestElement1(self, arr, k):
        arr.sort(reverse= True)

        return arr[k-1]

    # Min heap
    def kthLargestElement2(self, arr, k):
        heap = []

        for i in arr:
            heapq.heappush(heap, i)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]

obj = Solution()

arr = list(map(int, input().split()))

k = int(input())

print(obj.kthLargestElement1(arr, k))

print(obj.kthLargestElement2(arr, k))