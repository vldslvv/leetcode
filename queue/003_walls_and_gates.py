from typing import List, Tuple
from queue import Queue

INF = 2147483647
GATE = 0
WALL = -1
class Solution():
    def walls_and_gates(self, xs: List[List[int]]):
        for i in range(len(xs)):
            for j in range(len(xs[i])):
                if xs[i][j] == GATE:
                    self.bfs(xs, i, j)
    
    def get_directions(self, xs, i, j) -> List[Tuple[int, int]]:
        def append_if_room(m, n):
            if xs[m][n] != GATE and xs[m][n] != WALL:
                dir.append((m, n))
                
        dir = []
        if i > 0:
            append_if_room(i - 1, j)
        if i < len(xs) - 1:
            append_if_room(i + 1, j)
        if j > 0:
            append_if_room(i, j - 1)
        if j < len(xs[i]) - 1:
            append_if_room(i, j + 1)
        return dir

    def bfs(self, xs, start_i, start_j):
        visited = set()
        queue = Queue()
        dist = 0
        
        visited.add((start_i, start_j))
        queue.put((start_i, start_j))
            
        while not queue.empty():
            size = queue.qsize()
            for _ in range(size):
                i, j = queue.get()
                if xs[i][j] > dist or xs[i][j] == 0:
                    xs[i][j] = dist
                else:
                    continue
                
                directions = self.get_directions(xs, i, j)
                for d in directions:
                    if d not in visited:
                        visited.add(d)
                        queue.put(d)
            dist += 1
