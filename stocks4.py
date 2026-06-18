class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        INF = float('-inf')
        dp = [[[INF] * 2 for _ in range(k + 1)] for _ in range(n)]
        dp[0][0][0] = 0
        dp[0][0][1] = -prices[0]
        for i in range(1, n):
            for t in range(k + 1):
                dp[i][t][0] = dp[i - 1][t][0]
                if t > 0:
                    dp[i][t][0] = max(dp[i - 1][t][0], dp[i - 1][t - 1][1] + prices[i])
                dp[i][t][1] = max(dp[i - 1][t][1], dp[i - 1][t][0] - prices[i])
        ans = 0
        for t in range(k + 1):
            ans = max(ans, dp[n - 1][t][0])
        return ans

        
