from typing import List
import numpy as np


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = np.full((len(grid), len(grid[0])), np.iinfo(np.int32).max)
        dp[0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i > 0:
                    dp[i][j] = min(dp[i][j], grid[i][j] + dp[i - 1][j])
                    # print(f"dp[{i}][{j}]:{dp[i][j]}, case:{1}")
                if j > 0:
                    dp[i][j] = min(dp[i][j], grid[i][j] + dp[i][j - 1])
                    # print(f"dp[{i}][{j}]:{dp[i][j]}, case:{2}")

                if j < len(grid[0]) - 1:
                    dp[i][j] = min(dp[i][j], grid[i][j] + dp[i][j + 1])
                    # print(f"dp[{i}][{j}]:{dp[i][j]}, case:{3}")

                if i < len(grid) - 1:
                    dp[i][j] = min(dp[i][j], grid[i][j] + dp[i + 1][j])
                    # print(f"dp[{i}][{j}]:{dp[i][j]}, case:{4}")

                # print(f"dp[{i}][{j}]:{dp[i][j]}")

        return dp[len(grid) - 1][len(grid[0]) - 1]


sol = Solution()
print(sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(sol.minPathSum([[1, 2, 3], [4, 5, 6]]))
print(sol.minPathSum([[1]]))
print(sol.minPathSum([[1, 1], [1, 1]]))
