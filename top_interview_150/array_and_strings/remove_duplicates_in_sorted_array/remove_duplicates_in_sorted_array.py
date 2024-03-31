from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        current = 0
        finder = 0
        while finder < len(nums):
            if nums[finder] == nums[current]:
                finder += 1
                continue
            current += 1
            nums[current] = nums[finder]
        return current + 1


sol = Solution()
# print(sol.removeDuplicates([1, 1, 2]))
# print(sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
# print(sol.removeDuplicates([1]))
# print(sol.removeDuplicates([1, 2, 4]))
# print(sol.removeDuplicates([1, 2, 4, 4, 4]))
# print(sol.removeDuplicates([1, 2]))
# print(sol.removeDuplicates([1, 1]))
print(sol.removeDuplicates([]))
