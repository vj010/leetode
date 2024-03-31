from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        current, finder = 0, 0
        if len(nums) == 0:
            return 0
        while finder < len(nums):
            print(
                f"current:{current}, nums[current]:{nums[current]}, finder:{finder}, nums[finder]:{nums[finder]}"
            )
            if nums[finder] != val:
                nums[current] = nums[finder]
                current += 1
                finder += 1
                continue
            finder += 1

        return current


sol = Solution()
print(sol.removeElement([3, 2, 2, 3], 3))
print(sol.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
print(sol.removeElement([0], 0))
print(sol.removeElement([5, 5, 5, 5], 5))
print(sol.removeElement([], 5))
print(sol.removeElement([0], 5))
print(sol.removeElement([0, 0, 0, 0], 5))
print(sol.removeElement([4, 5], 5))
