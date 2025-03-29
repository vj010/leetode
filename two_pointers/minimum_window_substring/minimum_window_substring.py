from collections import Counter, deque


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        s_freq = Counter(s)
        t_freq = Counter(t)
        current_freq = {}
        unique_t = len(t_freq.keys())
        for k, v in t_freq.items():
            if k not in s_freq or s_freq[k] < t_freq[k]:
                return ""

        left = 0
        right = 0
        queue = deque()
        matches = 0
        min_len = 1000000
        min_left = 0
        min_right = 0

        for i in range(len(s)):
            if s[i] in t_freq:
                queue.append(i)

        while left < len(s) and s[left] not in t_freq:
            left += 1
        if left == len(s):
            return ""
        right = left

        while left < len(s) and right < len(s):
            if s[right] in t_freq:
                current_freq[s[right]] = (
                    current_freq[s[right]] + 1 if s[right] in current_freq else 1
                )
                if current_freq[s[right]] == t_freq[s[right]]:
                    matches += 1
                    while matches == unique_t:
                        str_len = right - left + 1
                        if min_len >= str_len:
                            min_left = left
                            min_right = right
                            min_len = str_len
                        if s[left] in current_freq:
                            current_freq[s[left]] -= 1
                            if current_freq[s[left]] < t_freq[s[left]]:
                                matches -= 1

                        queue.popleft()
                        if len(queue) > 0:
                            left = queue[0]
                        else:
                            while left < len(s) and s[left] not in t_freq:
                                left += 1
                            right = left

            right += 1

        return s[min_left : min_right + 1]


sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))

print(sol.minWindow("ABAA", "AA"))
print(sol.minWindow("A", "A"))

print(sol.minWindow("ABAADAC", "ADC"))
