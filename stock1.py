class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        ans = float('-inf')
        for i in range(len(prices)):
            profit = prices[i] - mini
            mini = min(mini, prices[i])
            ans = max(profit, ans)
        return ans

        
