from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [
            [[[False] * (n + 1) for _ in range(m + 1)] for _ in range(n + 1)]
            for _ in range(m + 1)
        ]
        # print(len(dp))
        # print(len(dp[0]))
        # print(len(dp[0][0]))
        # print(len(dp[0][0][0]))
        # print(dp[0][0][0][0])
        max_val = 0
        for i in range(m):
            for j in range(n):
                dp[i][j][1][1] = matrix[i][j] == "1"
                if dp[i][j][1][1]:
                    max_val = 1

        for i in range(m):
            for j in range(n):
                for k in range(2, m - i + 1):
                    dp[i][j][k][1] = dp[i][j][k - 1][1] and matrix[i + k - 1][j] == "1"
                    if dp[i][j][k][1]:
                        max_val = max(max_val, k)

        for i in range(m):
            for j in range(n):
                for k in range(2, n - j + 1):
                    dp[i][j][1][k] = dp[i][j][1][k - 1] and matrix[i][j + k - 1] == "1"
                    if dp[i][j][1][k]:
                        max_val = max(max_val, k)

        for k in range(2, m + 1):
            for l in range(2, n + 1):
                for i in range(m):
                    for j in range(n):
                        dp[i][j][k][l] = (
                            dp[i][j][k - 1][l - 1]
                            and dp[i + k - 1][j][1][l]
                            and dp[i][j + l - 1][k][1]
                        )
                        if dp[i][j][k][l]:
                            max_val = max(max_val, l * k)
        # print(dp[1][2][1][2])
        # print(dp[1][4][1][1])
        return max_val

    def __printMatrix(self, grid):
        for i in range(len(grid)):
            print(grid[i])


sol = Solution()
print(
    sol.maximalRectangle(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
    )
)

print("-------------------------------------------------------")
print(sol.maximalRectangle([["1"]]))

print("--------------------------------------------------------")
print(sol.maximalRectangle([["0"]]))


print("--------------------------------------------------------")

print(
    sol.maximalRectangle(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "1"],
            ["1", "1", "0", "1", "1"],
            ["0", "1", "1", "1", "1"],
            ["0", "1", "0", "0", "0"],
        ]
    )
)

print("-----------------------------------------------------------")

print(
    sol.maximalRectangle(
        [
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)
