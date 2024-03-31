from typing import List
import numpy as np


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        min_len, current_sum = 100000000, 0
        current_sum = 0
        left, right = 0, 0
        while right < len(nums):
            if right < len(nums):
                current_sum += nums[right]
                # print(f"adding:{nums[right]}, current_sum:{current_sum}")
            while current_sum >= target and left <= right:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                # print(f"min_len:{min_len}, left:{left}, right:{right}")
                left += 1
                if right >= len(nums):
                    break
            right += 1

        return min_len if min_len != 100000000 else 0


sol = Solution()
print(sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(sol.minSubArrayLen(4, [1, 4, 4]))
print(sol.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
print(sol.minSubArrayLen(8, [1, 1, 1, 1, 1, 1, 1, 1]))
print(sol.minSubArrayLen(8, [1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(sol.minSubArrayLen(1, [1, 1, 1, 1, 1, 1, 1, 1, 1]))
print(sol.minSubArrayLen(1, [1]))
print(sol.minSubArrayLen(7, [1]))
print(sol.minSubArrayLen(7, [5, 5]))
print(sol.minSubArrayLen(7, [5, 5, 4, 3, 6]))
