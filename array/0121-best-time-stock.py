from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                temp = max(prices[j] - prices[i], temp)
        return temp

    def maxProfit2(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for v in prices:
            min_price = min(min_price, v)
            max_profit = max(max_profit, v - min_price)
        return max_profit

prices = [7,1,5,3,6,4]
s = Solution()
print(s.maxProfit2(prices))