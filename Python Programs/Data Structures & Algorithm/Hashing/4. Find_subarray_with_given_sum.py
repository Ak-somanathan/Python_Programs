def subArraySum(self, arr, target):
    prefix_sum = 0
    seen = {0:[-1]}

    for i, num in enumerate(arr):
        prefix_sum += num
        need = prefix_sum - target

        if need in seen:
            for j in seen[need]:
                print(arr[j+1 : i+1])

        seen.setdefault(prefix_sum, []).append(i)

arr = list(map(int, input().split()))

target = int(input())

subArraySum(arr, target)