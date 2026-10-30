def lengthOfTheConsecutive2(arr):
    nums = set(arr)
    res =[]

    for i in nums:
        if i - 1 not in nums:
            curr = i
            sequence = [curr]
            while curr + 1 in nums:
                curr += 1
                sequence.append(curr)

            if len(sequence) > len(res):
                res = sequence

    return res

arr = list(map(int, input().split()))

print(lengthOfTheConsecutive2(arr))