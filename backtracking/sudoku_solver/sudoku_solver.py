from typing import List, Set
from collections import Counter, deque
from time import perf_counter


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows: List[Set[str]] = [set() for _ in range(len(board))]
        columns: List[Set[str]] = [set() for _ in range(len(board[0]))]
        subgrid: List[Set[str]] = [set() for _ in range(len(board[0]))]
        empty_cells = deque()

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty_cells.append((i, j))
                    continue
                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
                self.__insertInSubgrid(subgrid, i, j, board[i][j])

        # print(f"empty cells:{empty_cells}")

        if len(empty_cells) > 0:
            self.__solve(board, rows, columns, subgrid, empty_cells)
        # print(f"solution found:{solved}")
        self.__printBoard(board)
        # print(self.__checkSudoku(board))
        # print(rows)
        # print(columns)

    def __solve(
        self,
        board: List[List[str]],
        rows: List[Set[str]],
        cols: List[Set[str]],
        subgrid: List[Set[str]],
        empty_cells,
    ) -> bool:
        if len(empty_cells) == 0:
            return True

        next_empty_pos = empty_cells.popleft()
        i, j = next_empty_pos

        for m in range(1, 10):
            if self.__checkused(str(m), rows, cols, subgrid, i, j):
                continue
            board[i][j] = str(m)
            self.__markUsed(board[i][j], rows, cols, subgrid, i, j)

            if self.__solve(
                board,
                rows,
                cols,
                subgrid,
                empty_cells,
            ):
                return True

            self.__markFree(board[i][j], rows, cols, subgrid, i, j)
            board[i][j] = "."

        empty_cells.appendleft(next_empty_pos)
        return False

    def __checkused(
        self,
        num: str,
        rows: List[Set[str]],
        columns: List[Set[str]],
        subgrid: List[Set[str]],
        i: int,
        j: int,
    ) -> bool:
        if num in rows[i] or num in columns[j]:
            return True
        return self.__checkInSubgrid(subgrid, i, j, num)

    def __markUsed(
        self,
        num: str,
        rows: List[Set[str]],
        columns: List[Set[str]],
        subgrid: List[Set[str]],
        i: int,
        j: int,
    ) -> None:
        rows[i].add(num)
        columns[j].add(num)
        self.__insertInSubgrid(subgrid, i, j, num)

    def __markFree(
        self,
        num: str,
        rows: List[Set[str]],
        columns: List[Set[str]],
        subgrid: List[Set[str]],
        i: int,
        j: int,
    ) -> None:
        rows[i].remove(num)
        columns[j].remove(num)
        self.__removeFromSubgrid(subgrid, i, j, num)

    def __insertInSubgrid(
        self, subgrid: List[Set[str]], i: int, j: int, num: str
    ) -> None:
        subgrid_ind = 3 * (i // 3) + j // 3
        subgrid[subgrid_ind].add(num)

    def __removeFromSubgrid(
        self, subgrid: List[Set[str]], i: int, j: int, num: str
    ) -> None:
        subgrid_ind = 3 * (i // 3) + j // 3
        subgrid[subgrid_ind].remove(num)

    def __checkInSubgrid(
        self, subgrid: List[Set[str]], i: int, j: int, num: str
    ) -> bool:
        subgrid_ind = 3 * (i // 3) + j // 3
        return True if num in subgrid[subgrid_ind] else False

    def __printBoard(self, board):
        for i in range(len(board)):
            print(board[i])


sol = Solution()
c1_s = perf_counter()
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
print(perf_counter() - c1_s)
print("-------------------------------------------------------------------------")
c2_s = perf_counter()
sol.solveSudoku(
    [
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "9", ".", ".", "1", ".", ".", "3", "."],
        [".", ".", "6", ".", "2", ".", "7", ".", "."],
        [".", ".", ".", "3", ".", "4", ".", ".", "."],
        ["2", "1", ".", ".", ".", ".", ".", "9", "8"],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "2", "5", ".", "6", "4", ".", "."],
        [".", "8", ".", ".", ".", ".", ".", "1", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]
)
print(perf_counter() - c2_s)
