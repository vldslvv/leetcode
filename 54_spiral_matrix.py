from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return []
        m = len(matrix)
        n = len(matrix[0])
        spiral = []

        top_left = (0,0)
        bottom_right = (m - 1, n - 1)
        while True:
            border_spiral = self.solveBorders(matrix, top_left[0], top_left[1], bottom_right[0], bottom_right[1])
            spiral += border_spiral

            if len(border_spiral) <= 1:
                break

            top_left = (top_left[0] + 1, top_left[1] + 1)
            bottom_right = (bottom_right[0] - 1, bottom_right[1] - 1)
        
        return spiral


    def solveBorders(self, matrix, a1, a2, b1, b2) -> List:
        border_spiral = []
        if a1 > b1 or a2 > b2:
            return border_spiral

        # Top border left to right
        border_spiral += [matrix[a1][i] for i in range(a2, b2 + 1)]
        # Right border top to bottom
        border_spiral += [matrix[i][b2] for i in range(a1 + 1, b1)]
        if a1 == b1:
            return border_spiral
        # Bottom border right to left
        border_spiral += [matrix[b1][i] for i in range (b2, a2 - 1, -1)]
        if a2 == b2:
            return border_spiral
        # Left border top to bottom
        border_spiral += [matrix[i][a2] for i in range (b1 - 1, a1, -1)]

        return border_spiral


s = Solution()
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# matrix = [[1,2], [3,4]]
# matrix = [[1,2,3]]
# matrix = [[1]]
# matrix = [[1], [2], [3]]
res = s.spiralOrder(matrix)
print(res)
