from typing import List
import numpy as np
import math


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        dim = min(row, col)
        dp = np.zeros((dim + 1, row, col), dtype=bool)
        area = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "1":
                    dp[1][i][j] = True
                    area = 1

        for i in range(2, dim + 1):
            found = False
            for j in range(row):
                for k in range(col):
                    square = math.ceil(i / 2)
                    # print(f"square:{square}")
                    if j + (i // 2) >= row or k + (i // 2) >= col:
                        continue
                    dp[i][j][k] = (
                        dp[square][j][k]
                        and dp[square][j + (i // 2)][k]
                        and dp[square][j][k + (i // 2)]
                        and dp[square][j + (i // 2)][k + (i // 2)]
                    )
                    if dp[i][j][k]:
                        area = max(area, i * i)
                        found = True
            if not found:
                break
        return area


sol = Solution()
print(
    sol.maximalSquare(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
    )
)
print(sol.maximalSquare([["0", "1"], ["1", "0"]]))
print(sol.maximalSquare([["0"]]))
print(sol.maximalSquare([["1"]]))
print(sol.maximalSquare([["1", "1"], ["1", "1"]]))
print(sol.maximalSquare([["1", "0"], ["0", "0"], ["0", "0"]]))
print(sol.maximalSquare([["1", "1", "1"], ["1", "1", "1"], ["1", "1", "0"]]))
print(sol.maximalSquare([["1", "1", "1"], ["1", "1", "1"], ["1", "1", "1"]]))
print(sol.maximalSquare([["0", "0", "0"], ["1", "1", "1"], ["1", "1", "1"]]))
print(
    sol.maximalSquare(
        [
            ["1", "1", "1", "1"],
            ["1", "1", "1", "1"],
            ["1", "1", "1", "1"],
            ["1", "1", "1", "1"],
        ]
    )
)
print(
    sol.maximalSquare(
        [
            ["0", "1", "1", "1"],
            ["0", "1", "1", "1"],
            ["1", "1", "1", "1"],
            ["0", "1", "0", "1"],
        ]
    )
)
