# Hash map
nums = list(map(int, input().split()))
target = int(input())
seen = {}

for i,num in enumerate(nums):
    need = target - num
    if need in seen:
        print(seen[need], i)
        break
    seen[num] = i