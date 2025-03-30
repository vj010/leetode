import bisect


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        pos_map = {}
        for i in range(len(s)):
            if s[i] in pos_map:
                pos_map[s[i]].append(i)
            else:
                pos_map[s[i]] = [i]

        ans = 0
        # print(f"pos:{pos_map}")

        for i in range(len(s)):
            ind = bisect.bisect_left(pos_map[s[i]], i)
            # print(f"s[{i}]:{s[i]}, pos_map:{pos_map[s[i]][ind]}, ind:{ind}")
            if ind == 0:
                left = i - 0
            else:
                left = pos_map[s[i]][ind] - pos_map[s[i]][ind - 1] - 1

            if ind == len(pos_map[s[i]]) - 1:
                right = len(s) - 1 - i
            else:
                right = pos_map[s[i]][ind + 1] - pos_map[s[i]][ind] - 1

            # print(f"left:{left}, right:{right}")
            ans += (left + 1) * (right + 1)

        return ans


sol = Solution()
print(sol.uniqueLetterString("LEETCODE"))
print(sol.uniqueLetterString("ABA"))
print(sol.uniqueLetterString("ABC"))
print(sol.uniqueLetterString("LEETCODEC"))
print(sol.uniqueLetterString("AAC"))
