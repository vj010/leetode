import sys
from typing import List

sys.stdin = open("./dynamic_programming/generate_paranthesis/input.txt", "r")
sys.stdout = open("./dynamic_programming/generate_paranthesis/output.txt", "w")


class Solution:
    @staticmethod
    def __get_paranthesis_str(num, min_paranthesis):
        closing_brackets = 0
        paranthesis = []
        x = num
        cnt = 0
        while x > 0:
            cnt = cnt + 1 if x & 1 == 1 else cnt
            x >>= 1
        if cnt < min_paranthesis:
            return ""
        # print(f"getting paranthesis str for num :{num}")
        while num > 0:
            if num & 1 == 1:
                closing_brackets -= 1
                paranthesis.append("(")
            else:
                closing_brackets += 1
                paranthesis.append(")")
            if closing_brackets < 0:
                return ""
            num >>= 1
        if closing_brackets != 0:
            return ""
        return "".join(paranthesis[::-1])

    @staticmethod
    def get_paranthesis_list(n):
        paranthesis_list = []
        for i in range(2 ** (2 * n) + 1):
            paranthesis_str = Solution.__get_paranthesis_str(i, n)
            if len(paranthesis_str) > 0:
                paranthesis_list.append(paranthesis_str)
        return paranthesis_list


n = int(input().strip())
print(Solution.get_paranthesis_list(n))
