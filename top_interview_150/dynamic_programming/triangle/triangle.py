from typing import List
import numpy as np


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = np.zeros((len(triangle) + 1, len(triangle)), dtype=int)
        dp[1][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                current_val = np.inf
                if j > 0 and j <= len(triangle[i - 1]):
                    current_val = min(triangle[i][j] + dp[i][j - 1], current_val)
                if j < len(triangle[i - 1]):
                    current_val = min(triangle[i][j] + dp[i][j], current_val)
                dp[i + 1][j] = current_val

        # print(f"dp:{dp}")

        return np.min(dp[len(triangle)])


sol = Solution()
print(sol.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(sol.minimumTotal([[9], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(sol.minimumTotal([[9]]))
print(sol.minimumTotal([[9], [1, -100]]))
print(sol.minimumTotal([[-100]]))
print(sol.minimumTotal([[0], [1, 3], [-4, 5, -9], [1, 2, 13, 5]]))
