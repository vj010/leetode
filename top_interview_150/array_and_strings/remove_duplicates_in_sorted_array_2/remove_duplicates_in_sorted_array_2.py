from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current, finder, current_count, prev_val = 0, 0, 0, -1
        while finder < len(nums):
            # print(
            #     f"nums[current]:{nums[current]}, current_count:{current_count},nums[finder]:{nums[finder]}"
            # )
            if current_count < 2 or nums[finder] != prev_val:
                if nums[finder] != prev_val:
                    current_count = 0
                nums[current] = nums[finder]
                prev_val = nums[current]
                finder += 1
                current += 1
                current_count += 1
                continue
            finder += 1

        # print(f"nums:{nums}")
        return current


sol = Solution()
print(sol.removeDuplicates([1, 1, 2]))
print(sol.removeDuplicates([1, 1, 1, 2]))
# print(sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(sol.removeDuplicates([1]))
print(sol.removeDuplicates([1, 2, 4]))
print(sol.removeDuplicates([1, 2, 4, 4, 4]))
print(sol.removeDuplicates([1, 2]))
print(sol.removeDuplicates([1, 1]))
print(sol.removeDuplicates([1, 1, 1, 2, 2, 3]))
print(sol.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
