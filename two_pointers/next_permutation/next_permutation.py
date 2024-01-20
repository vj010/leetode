from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = -1
        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(nums) - 1, i, -1):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    pos = i
                    break

        if pos == -1:
            nums.reverse()
            return

    @staticmethod
    def quick_sort(nums: List[int], start: int, end: int) -> None:
        print("calling quick sort", nums, nums[end])
        if end <= start:
            return
        pivot = nums[end]
        partition = Solution.get_partition(nums, start, end, pivot)
        Solution.quick_sort(nums, start, partition - 1)
        Solution.quick_sort(nums, partition + 1, end)

    @staticmethod
    def get_partition(nums: List[int], start: int, end: int, pivot: int) -> int:
        i = start
        j = end - 1
        while True:
            # print(f"i:{i}, j:{j}, start:{start}, end:{end}, pivot:{pivot}")
            while nums[i] <= pivot and i < end:
                i += 1
            while j > 0 and nums[j] > pivot:
                j -= 1
            if i >= j:
                break
            else:
                nums[i], nums[j] = nums[j], nums[i]
        nums[i], nums[end] = nums[end], nums[i]
        return i


Solution.quick_sort([1, 1, 1, 1, 2], 0, 4)
