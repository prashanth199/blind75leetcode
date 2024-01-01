class Solution:

    def __init__(self,prices) -> None:
        self.result = self.getMaximumProfit(prices)

    def getMaximumProfit(self,prices):
        # 
        n = len(prices)
        min_buy_price = prices[0]
        max_profit = 0

        for i in range(1,n):
            current_profit = prices[i] - min_buy_price

            max_profit = max(current_profit,max_profit)

            min_buy_price = min(prices[i],min_buy_price)
        return max_profit




