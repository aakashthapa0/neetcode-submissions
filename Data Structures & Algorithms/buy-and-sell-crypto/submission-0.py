class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        best = 0
        for price in prices[1:]:
            profit = price - min_price
            best = max(best, profit)
            min_price = min(min_price, price)
        return best