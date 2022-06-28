from typing import List, Tuple
from queue import Queue


LAND = '1'
WATER = '0'
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands_visited = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == LAND:
                    islands_visited += 1
                    self.bfs(grid, i, j)
                    continue
        
        return islands_visited
    
    def get_directions(self, grid, i, j):
        dir = []
        if i > 0 and grid[i - 1][j] == LAND:
            dir.append((i - 1, j))
        if i < len(grid) - 1 and grid[i + 1][j] == LAND:
            dir.append((i + 1, j))
        if j > 0 and grid[i][j - 1] == LAND:
            dir.append((i, j - 1))
        if j < len(grid[i]) - 1 and grid[i][j + 1] == LAND:
            dir.append((i, j + 1))
        return dir
    
    def bfs(self, grid: List[List[str]], i: int, j: int):
        queue = Queue()
        queue.put((i, j))
        grid[i][j] = '-1'

        while not queue.empty():
            size = queue.qsize()
            for _ in range(size):
                qi, qj = queue.get()
                directions = self.get_directions(grid, qi, qj)
                for d in directions:
                    grid[d[0]][d[1]] = '-1'
                    queue.put(d)
 