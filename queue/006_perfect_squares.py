import math
from collections import deque

class Solution:
    def __init__(self):
        self.squares = {}
        
    def get_largest_square(self, n) -> int:
        return math.floor(math.sqrt(n))
    
    def numSquares(self, n: int) -> int:
        # Start with root
        # N - largest square (take square root and floor it)
        # N - second largest square
        # complete until 0
        step = 0
        q = deque([(n, 0)])
        visited = set()
        
        while q:
            size = len(q)
            for _ in range(size):
                number, operand = q.popleft()
                subtracted = number - operand

                if subtracted == 0:
                    return step
                if subtracted < 0 or subtracted in visited:
                    continue
                
                visited.add(subtracted)

                largest_square = self.get_largest_square(n)
                next_nodes = [(subtracted, self.square(x)) for x in range(largest_square, 0, -1)]
                q.extend(next_nodes)
                
            step += 1

        pass

    def square(self, n):
        existing = self.squares.get(n, -1)
        if existing > 0:
            return existing
        val = n * n
        self.squares[n] = val
        return val
        