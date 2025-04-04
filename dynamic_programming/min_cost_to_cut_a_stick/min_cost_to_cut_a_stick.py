from typing import Dict, List, Tuple
import bisect


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        mem: Dict[Tuple[int, int], int] = {}
        cuts = list(set(cuts))
        cuts.sort()
        ans = self.__calculate(0, n, cuts, mem)
        return ans

    def __calculate(
        self, l: int, r: int, cuts: List[int], mem: Dict[Tuple[int, int], int]
    ) -> int:
        if r - l <= 1:
            return 0
        if (l, r) in mem:
            return mem[(l, r)]
        m, n = self.__getCuts(l + 1, r - 1, cuts)
        ans = 10000000
        if m > n:
            ans = 0
        final_ans = 0
        for i in range(m, n + 1):
            first_part, second_part = self.__getRanges(cuts, i, l, r)
            ans = min(
                ans,
                r
                - l
                + self.__calculate(
                    first_part[0],
                    first_part[1],
                    cuts,
                    mem,
                )
                + self.__calculate(second_part[0], second_part[1], cuts, mem),
            )
        final_ans += ans

        mem[(l, r)] = final_ans
        # print(f"l:{l} r:{r}, cost:{mem[(l,r)]}")
        return mem[(l, r)]

    def __getCuts(self, l, r, cuts) -> Tuple[int, int]:
        m = bisect.bisect_left(cuts, l)
        n = bisect.bisect_right(cuts, r)
        if m >= len(cuts) or n <= 0 or m > n:
            return (-1, -2)
        # print(f"in function m:{m}, n:{n}")
        return (m, n - 1)

    def __getRanges(
        self, cuts: List[int], i: int, l: int, r: int
    ) -> List[Tuple[int, int]]:
        return [(l, cuts[i]), (cuts[i], r)]

    def tet_getCuts(self):
        m, n = self.__getCuts(0, 5, [1, 2, 3, 4])
        print(f"m:{m}, {n}")
        m, n = self.__getCuts(5, 5, [1, 2, 3, 4])
        print(f"m:{m}, {n}")
        m, n = self.__getCuts(2, 5, [3, 7, 9])
        print(f"m:{m}, {n}")
        m, n = self.__getCuts(1, 2, [3, 4, 5])
        print(f"m:{m}, {n}")


sol = Solution()
# sol.tet_getCuts()
print(sol.minCost(9, [5, 6, 1, 4, 2]))
print(sol.minCost(7, [1, 3, 4, 5]))
print(sol.minCost(5, []))
