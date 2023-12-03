from typing import List, Tuple


def is_on_edge(m: int, n: int, pos: Tuple[int, int]) -> bool:
    # Maybe not be super efficient
    return pos[0] == 0 or pos[0] == m - 1 or pos[1] == 0 or pos[1] == n - 1


def mark_if_surrounded_dfs(board: List[List[str]], m: int, n: int, start: Tuple[int, int]) -> set:
    visited = set()
    stack = [start]
    is_surrounded = True


    while len(stack) != 0:
        current = stack.pop()
        if current not in visited:
            visited.add(current)

            if is_on_edge(m, n, current):
                is_surrounded = False

            # Get adjacent Os
            c = current
            # Left, right, up, down directions
            adjacent = ((c[0] - 1, c[1]), (c[0] + 1, c[1]), (c[0], c[1] + 1), (c[0], c[1] - 1))
            # Only the ones on board and Os
            adjacent = [el for el in adjacent if el[0] >= 0 and el[0] < m and el[1] >= 0 and el[1] < n and board[el[0]][el[1]] == "O"]
            

            stack.extend(adjacent)

    # Capture if surrounded
    if is_surrounded:
        for el in visited:
            board[el[0]][el[1]] = "X"

    return visited


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # First, find O and then find any connected Os to it
        # If any of the Os is adjacent to a border, a region is not surrounded
        # Otherwise, capture the region with Xs

        # Find dimentions first
        m = len(board)
        if m <= 1:
            return
        n = len(board[m - 1])
        if n <= 1:
            return

        visited_clusters = set()
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited_clusters and board[i][j] == "O":
                    # Do dfs here and mark visited
                    cluster = mark_if_surrounded_dfs(board, m, n, (i, j))
                    visited_clusters = visited_clusters.union(cluster)



board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# board = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# board = [["O"]]
# board = [["O","O"],["O","O"]]
s = Solution()
res = s.solve(board)
print(board)