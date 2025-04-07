from typing import List, Tuple
from functools import cmp_to_key
from queue import PriorityQueue


def cmp(a: Tuple[int, int], b: Tuple[int, int]):
    if a[0] != b[0]:
        return a[0] - b[0]
    else:
        return a[1] - b[1]


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        list_count = len(nums)
        final_list = []
        pq = PriorityQueue()
        se_points = []
        for i in range(list_count):
            for x in nums[i]:
                pq.put((x, i))
        while not pq.empty():
            final_list.append(pq.get())
        start = 0
        end = 0
        el_map = {}
        current_list_count = 0
        start_min = final_list[0][0]
        end_min = final_list[-1][0]
        # print(f"final_list:{final_list}")

        while start <= end and start < len(final_list) and end < len(final_list):
            if final_list[end][1] not in el_map or el_map[final_list[end][1]] <= 0:
                current_list_count += 1
                el_map[final_list[end][1]] = 1
            else:
                el_map[final_list[end][1]] += 1
            # print(f"start:{start}, end:{end} ,el_map:{el_map}")

            while list_count == current_list_count and start <= end:
                # print(f"found all lists start:{start}, end:{end} ,el_map:{el_map}")
                if self.__shorter_range(
                    final_list[start][0], final_list[end][0], start_min, end_min
                ):
                    start_min = final_list[start][0]
                    end_min = final_list[end][0]
                el_map[final_list[start][1]] -= 1
                if el_map[final_list[start][1]] <= 0:
                    current_list_count -= 1
                start += 1

            end += 1

        # print(f"final_list:{final_list}")

        return [start_min, end_min]

    def __shorter_range(self, a, b, s, e) -> bool:
        if b - a < e - s:
            return True
        elif b - a == e - s and a < s:
            return True

        return False


sol = Solution()
print(sol.smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
print(sol.smallestRange([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
print(sol.smallestRange([[1, 2, 3]]))
print(sol.smallestRange([[7]]))
print(sol.smallestRange([[1, 2, 3], [1, 2, 3]]))
print(sol.smallestRange([[1, 2, 3], [4, 5, 6], [6, 7, 8, 9]]))
print(sol.smallestRange([[1], [4], [6, 7, 8, 9]]))
