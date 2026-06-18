class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            if i == 1:
                dp[i][1] = max(dp[i - 1][1], -prices[i])
            else:
                dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        # ante undhu rozu ammesthe we can't buy ivala cuz of the cool down, so day before yesterday ammesindhi consider chestamu
        return dp[n - 1][0]

# the one with cooldown
