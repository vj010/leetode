from typing import List
import numpy as np


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-2000] * 3 for i in range(len(prices))]

        dp[0][0] = -1 * prices[0]
        dp[0][1] = 0
        dp[0][2] = 0

        max_profit = 0

        for i in range(1, len(prices)):
            dp[i][0] = max(
                dp[i - 1][0],
                dp[i - 2 if i > 1 else i - 1][1] - prices[i],
            )
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1])

            # print(f"dp:{dp[i]}")
        return max(dp[len(prices) - 1][1], dp[len(prices) - 1][2])


sol = Solution()
# print(sol.maxProfit([1, 2, 3, 0, 2]))
# print(sol.maxProfit([1, 1, 1, 1, 1]))
print(sol.maxProfit([1, 3, 2, 0, 1, 6, 1]))
# print(sol.maxProfit([1]))
print(sol.maxProfit([5, 2]))
