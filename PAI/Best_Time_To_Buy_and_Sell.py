from pip import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                result += prices[i + 1] - prices[i]
        return result
    def maxProfit2(self, prices: List[int]) -> int:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit2([7, 1, 5, 3, 6, 4]))