
# METHOD - 1 (Greedy works cuz we have infinite moves)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]
        return profit



# METHOD - 2 (must know)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        # here, 
        # dp[i][0] ante max profit attainable after processing days 0, 1, 2 ... i while not holding stock on i th day
        # dp[i][1] ante max profit attainable after processing days 0, 1, 2 ... i while holding the stock on i th day
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            # --> mundhu rozu kuda ledu or eroju ammesa
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i]) 
            #  --> mundhu rozu undi or eeroju konukunna
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]
        



        
