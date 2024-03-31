from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            print(nums1)
            return
        for i in range(m - 1, -1, -1):
            print(f"n+i:{n+i}")
            nums1[n + i] = nums1[i]
        i, j = 0, 0
        k = n
        while k < m + n and j < n:
            if nums1[k] > nums2[j]:
                print(f"i:{i}, j:{j} , k:{k}")
                nums1[i] = nums2[j]
                i += 1
                j += 1
                continue
            nums1[i] = nums1[k]
            k += 1
            i += 1

        while k < m + n:
            nums1[i] = nums1[k]
            k += 1
            i += 1
        while j < n:
            print(f"i:{i}, j:{j}")
            nums1[i] = nums2[j]
            i += 1
            j += 1
        print(nums1)


sol = Solution()
sol.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
sol.merge([1], 1, [0], 0)
sol.merge([0], 0, [1], 1)
sol.merge([5, 8, 9, 0, 0, 0], 3, [2, 5, 6], 3)
sol.merge([1, 2, 3, 0, 0, 0], 3, [3, 3, 3], 3)
