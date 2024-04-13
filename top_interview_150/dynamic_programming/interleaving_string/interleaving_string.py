from typing import List
import numpy as np


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s2) + len(s1):
            return False
        dp = np.zeros((len(s3) + 1, len(s1) + 1, len(s2) + 1), dtype=bool)
        dp[0] = np.ones((len(s1) + 1, len(s2) + 1), dtype=bool)
        for i in range(1, len(s3) + 1):
            for j in range(0, i + 1):
                k = j
                m = i - k
                # print(f"k:{k},m:{m}")
                if k > len(s1) or m > len(s2):
                    continue
                if k > 0:
                    dp[i][k][m] = (
                        True
                        if dp[i - 1][k - 1][m] and s3[i - 1] == s1[k - 1]
                        else False
                    )
                    # print(f"k:{k},m:{m}")
                    # print(
                    #     f"({dp[i][k][m]})dp[{i - 1}][{k - 1}][{m}]:{dp[i - 1][k - 1][m]}, s3[{i - 1}] == s1[{k - 1}]:{s3[i - 1] == s1[k - 1]}"
                    # )
                if m > 0:
                    dp[i][k][m] = (
                        True
                        if dp[i][k][m]
                        or (dp[i - 1][k][m - 1] and s3[i - 1] == s2[m - 1])
                        else False
                    )
                    # print(f"k:{k},m:{m}")
                    # print(
                    #     f"({dp[i][k][m]})dp[{i - 1}][{k}][{m - 1}]:{dp[i - 1][k][m - 1]}, s3[{i - 1}] == s2[{m - 1}]:{s3[i - 1] == s2[m - 1]}"
                    # )
        # print(dp)
        ans = np.any(dp[len(s3)])
        return bool(ans)


sol = Solution()
print(sol.isInterleave("aabcd", "abca", "abaacbcda"))
print(sol.isInterleave("aabcd", "", "aabcd"))
print(sol.isInterleave("", "aabcd", "aabcd"))
print(sol.isInterleave("", "", ""))
print(sol.isInterleave("ab", "ab", "aabb"))
print(sol.isInterleave("ab", "ab", "bbaa"))
print(sol.isInterleave("ab", "ab", "abba"))
print(sol.isInterleave("abc", "ab", "abcab"))
print(sol.isInterleave("a", "a", "aa"))
print(sol.isInterleave("a", "b", "ba"))
print(sol.isInterleave("a", "b", "ab"))
print(sol.isInterleave("", "b", "a"))
print(sol.isInterleave("", "b", "b"))
print(sol.isInterleave("aaabaa", "aaabbba", "aaaaabbabbaaa"))
print(sol.isInterleave("aaabaa", "", "aaaaa"))
