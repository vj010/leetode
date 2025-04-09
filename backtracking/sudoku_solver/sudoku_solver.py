from typing import List, Set
from collections import Counter, deque


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows: List[Set[str]] = [set() for _ in range(len(board))]
        columns: List[Set[str]] = [set() for _ in range(len(board[0]))]
        empty_cells = deque()

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty_cells.append((i, j))
                    continue
                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
        # print(f"empty cells:{empty_cells}")

        if len(empty_cells) > 0:
            self.__solve(board, rows, columns, empty_cells)
        # print(f"solution found:{solved}")
        # self.__printBoard(board)
        # print(self.__checkSudoku(board))
        # print(rows)
        # print(columns)

    def __solve(
        self,
        board: List[List[str]],
        rows: List[Set[str]],
        cols: List[Set[str]],
        empty_cells,
    ) -> bool:
        if len(empty_cells) == 0:
            return self.__checkSudoku(board)

        next_empty_pos = empty_cells.popleft()
        i, j = next_empty_pos

        for m in range(1, 10):
            if self.__checkused(str(m), board, rows, cols, i, j):
                continue
            board[i][j] = str(m)
            self.__markUsed(board[i][j], rows, cols, i, j)

            if self.__solve(
                board,
                rows,
                cols,
                empty_cells,
            ):
                return True

            self.__markFree(board[i][j], rows, cols, i, j)
            board[i][j] = "."

        empty_cells.appendleft(next_empty_pos)
        return False

    def __checkSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            counter = Counter(board[i])
            if len(counter) != 9 or "." in counter:
                # print("here1")
                return False
        for j in range(9):
            counter = Counter([board[i][j] for i in range(9)])
            if len(counter) != 9 or "." in counter:
                # print("here2")
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                val_map = {}
                for l in range(i, i + 3):  #
                    for k in range(j, j + 3):
                        if board[l][k] in val_map or board[l][k] == ".":
                            # print("here3")
                            return False
                        val_map[board[l][k]] = True

        return True

    def __checkused(
        self,
        num: str,
        board: List[List[str]],
        rows: List[Set[str]],
        columns: List[Set[str]],
        i: int,
        j: int,
    ) -> bool:
        if num in rows[i] or num in columns[j]:
            return True
        subgrid_i = 3 * (i // 3)
        subgrid_j = 3 * (j // 3)
        for l in range(subgrid_i, subgrid_i + 3):
            for m in range(subgrid_j, subgrid_j + 3):
                if board[l][m] == num:
                    return True
        return False

    def __markUsed(
        self, num: str, rows: List[Set[str]], columns: List[Set[str]], i: int, j: int
    ) -> None:
        rows[i].add(num)
        columns[j].add(num)

    def __markFree(
        self, num: str, rows: List[Set[str]], columns: List[Set[str]], i: int, j: int
    ) -> None:
        rows[i].remove(num)
        columns[j].remove(num)

    def __printBoard(self, board):
        for i in range(len(board)):
            print(board[i])


sol = Solution()
sol.solveSudoku(
    [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
)
