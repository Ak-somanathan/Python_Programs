class Solution:
    def subarrayBitwiseORs(self, arr : list[int]) -> int:
        res = set()
        prev = set()

        for num in arr:
            curr = {num}

            for val in prev:
                curr.add(val | num)
            
            res.update(curr)
            prev = curr
        
        return len(res)

obj = Solution()

arr = list(map(int, input().split()))

print(obj.subarrayBitwiseORs(arr))