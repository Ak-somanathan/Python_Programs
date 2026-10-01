# one pass
def bestTimetToBuyAndSell(arr):
    min_price = float('inf')
    max_profit = 0
    for i in arr:
        min_price = min(min_price, i)
        max_profit = max(max_profit, i - min_price)

    return max_profit

print(bestTimetToBuyAndSell(arr=list(map(int, input().split()))))
