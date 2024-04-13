from typing import List
import numpy as np


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s2) + len(s1):
            return False
        dp = np.zeros((len(s1) + 1, len(s2) + 1), dtype=bool)
        dp[0][0] = True
        for i in range(0, len(s1) + 1):
            for j in range(0, len(s2) + 1):
                if i > 0:
                    # print("here")
                    dp[i][j] = dp[i - 1][j] and s3[i + j - 1] == s1[i - 1]

                if j > 0 and not dp[i][j]:
                    dp[i][j] = dp[i][j - 1] and s3[i + j - 1] == s2[j - 1]

                if i + j == len(s3) and dp[i][j]:
                    return True
        return False


sol = Solution()
print(sol.isInterleave("aabcd", "abca", "abaacbcda"))
print(sol.isInterleave("aabcd", "", "aabcd"))
print(sol.isInterleave("", "aabcd", "aabcd"))
print(sol.isInterleave("", "", ""))
print(sol.isInterleave("ab", "ab", "aabb"))
# print(sol.isInterleave("ab", "ab", "bbaa"))
# print(sol.isInterleave("ab", "ab", "abba"))
# print(sol.isInterleave("abc", "ab", "abcab"))
# print(sol.isInterleave("a", "a", "aa"))
# print(sol.isInterleave("a", "b", "ba"))
# print(sol.isInterleave("a", "b", "ab"))
# print(sol.isInterleave("", "b", "a"))
# print(sol.isInterleave("", "b", "b"))
# print(sol.isInterleave("aaabaa", "aaabbba", "aaaaabbabbaaa"))
# print(sol.isInterleave("aaabaa", "", "aaaaa"))
# print(sol.isInterleave("aabcc", "dbbca", "aadbbbaccc"))
print(sol.isInterleave("aacaac", "aacaaeaac", "aacaaeaaeaacaac"))
