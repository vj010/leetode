import sys
from typing import List
import numpy as np

sys.stdin = open("./dynamic_programming/jump_game2/input.txt", "r")
sys.stdout = open("./dynamic_programming/jump_game2/output.txt", "w")


class Solution:
    @staticmethod
    def get_min_steps(nums: List[int]) -> int:
        # print(nums)
        dp = [np.inf] * len(nums)
        # print(dp)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(i, min(nums[i] + i + 1, len(nums))):
                dp[j] = min(dp[j], dp[i] + 1)
            # print(dp)
        return int(dp[len(nums) - 1])


nums = list(map(int, input().strip().split(" ")))
print(Solution.get_min_steps(nums))
