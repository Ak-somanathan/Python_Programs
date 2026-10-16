class Solution:
    # linear traversal 
    def evenOddIntegers1(self, arr):
        even = 0
        odd = 0
        for i in arr:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1

        return f"Even: {even}, Odd: {odd}"

    # sum method
    def evenOddIntegers2(self, arr):
        even = sum(1 for i in arr if i % 2 == 0)
        odd = sum(1 for i in arr if i % 2 != 0)

        return f"Even: {even}, Odd: {odd}"

    # single traversal using dictionary
    def evenOddIntegers3(self, arr):
        count = {"even": 0, "odd": 0}

        for i in arr:
            if i % 2 == 0:
                count["even"] +=1
            else:
                count["odd"] += 1
    
        return count

    # count + complement
    def evenOddIntegers4(self, arr):
        even = sum(1 for i in arr if i % 2 == 0)
        odd = len(arr) - even

        return f"Even: {even}, Odd: {odd}"

arr = list(map(int, input().split()))
obj = Solution()
print(obj.evenOddIntegers1(arr))
print(obj.evenOddIntegers2(arr))
print(obj.evenOddIntegers3(arr))
print(obj.evenOddIntegers4(arr))
        
    