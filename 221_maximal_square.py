from typing import List, Tuple, Dict


class Solution:
    max_len = 0

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        self.max_len = 0
        self.dp(0, 0, matrix, m)

        return self.max_len ** 2

    # i, j -- position to check
    # m -- memoized max length with key (i, j)
    # max_len
    def dp(self, i: int, j: int, matrix: List[List[str]], m: List[List[int]]) -> int:
        if i >= len(matrix) or j >= len(matrix[0]):
            return 0

        if m[i][j] != -1:
            return m[i][j]
        
        # It's necessary to step further even though we're not going to use those values in this node
        # But max_len will still be calculated
        right = self.dp(i, j + 1, matrix, m)
        down_right = self.dp(i + 1, j + 1, matrix, m)
        down = self.dp(i + 1, j, matrix, m)

        sq_len = 0
        if matrix[i][j] == "1":
            sq_len = 1 + min(right, down_right, down)

        if self.max_len < sq_len:
            self.max_len = sq_len

        m[i][j] = sq_len

        return sq_len

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Start from bottom-right square
        m = [[-1 * len(matrix[0])] for _ in range(len(matrix))]
        pass

        

s = Solution()
# matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix = [["1","0"],
          ["1","1"],
          ["1","1"]]
# matrix = [["0","1","1"],["1","1","1"]]
res = s.maximalSquare(matrix)
print(res)