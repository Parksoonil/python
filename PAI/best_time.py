from pip import List
def maxprofit(prices: List[int]) -> int:
    min_p = max(prices)
    result = 0
    for p in prices:
        min_p = min(p, min_p)
        result = max(result, p - min_p)
    return result
print(maxprofit([7, 1, 5, 3, 6, 4]))

def maxprofit2(prices: List[int]) -> int:
    max_p = 0
    for i, p in enumerate(prices):
        for j in range(i, len(prices)):
            max_p = max(prices[j] - p, max_p)
    return max_p
print(maxprofit2([7, 1, 5, 3, 6, 4]))

