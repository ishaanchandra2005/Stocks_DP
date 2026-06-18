# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         INF = float('-inf')
#         dp = [[[INF] * 2 for _ in range(3)] for _ in range(n)]

#         # dp[i][t][0] = max profit after day i, having completed t transactions, NOT holding stock
#         # dp[i][t][1] = max profit after day i, having completed t transactions, HOLDING stock

#         dp[0][0][0] = 0
#         dp[0][0][1] = -prices[0]
#         # states exactly same stocks 2 laaga cheyy
#         for i in range(1, n):
#             for t in range(3):
#                 dp[i][t][0] = dp[i - 1][t][0]
#                 if t > 0:
#                     dp[i][t][0] = max(dp[i - 1][t][0], dp[i - 1][t - 1][1] + prices[i])
#                 dp[i][t][1] = max(dp[i - 1][t][1], dp[i - 1][t][0] - prices[i])
#         ans = 0
#         for t in range(3):
#             ans = max(ans, dp[n - 1][t][0])
#         return ans


class Solution:
    def maxProfit(self, prices):
        NEG = float('-inf')
        prev = [[NEG] * 2 for _ in range(3)]
        prev[0][0] = 0
        prev[0][1] = -prices[0]
        for i in range(1, len(prices)):
            cur = [[NEG] * 2 for _ in range(3)]
            for t in range(3):
                cur[t][0] = prev[t][0]
                if t > 0:
                    cur[t][0] = max(
                        cur[t][0],
                        prev[t - 1][1] + prices[i]
                    )
                cur[t][1] = max(
                    prev[t][1],
                    prev[t][0] - prices[i]
                )
            prev = cur
        return max(prev[t][0] for t in range(3))
