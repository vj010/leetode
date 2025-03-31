from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            j = i
            while nums[j] != j + 1 and nums[j] > 0 and nums[j] <= len(nums):
                temp = nums[j]
                if nums[j] == nums[temp - 1]:
                    break
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp

        # print(f"nums:{nums}")

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1
