# three reversal technique - right 
arr = [1, 2, 3, 4, 5, 6, 7]
K = 3
n = len(arr)
K %= n
def reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

reverse(arr, 0, n - 1)
reverse(arr, 0, K - 1)
reverse(arr, K, n - 1)

print(arr)

# three reversal technique - left
arr = [1, 2, 3, 4, 5, 6, 7]
K = 3
n = len(arr)
K %= n
def reverse(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

reverse(arr, 0, K - 1)
reverse(arr, K, n - 1)
reverse(arr, 0, n - 1)

print(arr)