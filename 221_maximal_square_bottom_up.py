from typing import List, Tuple, Dict


class Solution:
    max_len = 0

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Extend memo matrix to simplify base cases
        m = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        self.max_len = 0

        # Start from the base case that lies in the bottom-right corner
        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, -1, -1):
                if matrix[i][j] == '1':
                    m[i][j] = 1 + min(m[i+1][j], m[i+1][j+1], m[i][j+1])
                else:
                    m[i][j] = 0

                if self.max_len < m[i][j]:
                    self.max_len = m[i][j]


        return self.max_len ** 2


        

s = Solution()
# matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix = [["1","0"],
          ["1","1"],
          ["1","1"]]
# matrix = [["0","1","1"],["1","1","1"]]
res = s.maximalSquare(matrix)
print(res)