from typing import List, Tuple


class Solution:
    def totalNQueens(self, n: int) -> int:
        # For each column or row, place one queen
        # If a queen cannot be placed, backtrack
        solutions = self.backtrack(0, [], n, 0)

        return solutions

    def backtrack(self, row_id: int, queens: List[Tuple[int, int]], n: int, num_solutions: int) -> int:
        if row_id == n:
            return num_solutions + 1

        new_solutions = num_solutions
        for i in range(0, n):
            pos = (row_id, i)
            if self.is_available(pos, queens, n):
                new_solutions += self.backtrack(row_id=row_id + 1, queens=queens + [pos], n=n, num_solutions=num_solutions)

        return new_solutions

    def is_available(self, pos: Tuple[int, int], queens: List[Tuple[int, int]], n: int) -> bool:
        for q_pos in queens:
            # Check rows
            if q_pos[0] == pos[0] or q_pos[1] == pos[1]:
                return False
            # Check positive diagonal by checking j - i
            if q_pos[1] - q_pos[0] == pos[1] - pos[0]:
                return False
            # Check negative diagonal by checking n - i - j -1
            if n - 1 - q_pos[0] - q_pos[1] == n - 1 - pos[0] - pos[1]:
                return False

        return True

s = Solution()
n = 10
res = s.totalNQueens(n)
print(res)
# pos = (3, 3)
# queens = [(0, 1), (2, 1)]
# assert s.is_available(pos=pos, queens=queens, n=n)
# assert not s.is_available((1, 1), [(0, 0)], n)
# assert not s.is_available((2, 1), [(1, 0)], n)
# assert not s.is_available((1, 1), [(0, 2)], n)
