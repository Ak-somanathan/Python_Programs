# kadane's algorithm - printing both subarray and sum
def maxSubarrarysum(arr):
    curr = maxi = arr[0]
    start = 0
    best_start = 0
    best_end = 0

    for i in range(1, len(arr)):
        if arr[i] > curr + arr[i]:
            curr = arr[i]
            start = i
        else:
            curr += arr[i]

        if curr > maxi:
            maxi = curr
            best_start = start
            best_end = i

    return arr[best_start:best_end+1]

# kadane's algorithm - sum
def subarraySum(arr):
    curr = arr[0]
    maxi = arr[0]
    for num in arr:
        curr = max(num, curr + num)
        maxi = max(curr, maxi)
    return maxi

arr=list(map(int, input().split()))

print(subarraySum(arr))
print(maxSubarrarysum(arr))