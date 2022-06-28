from multiprocessing.connection import wait
from queue import Queue


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = Queue(size)
        self.k = size
        self.sum = 0
        self.len = 0

    def next(self, a: int) -> float:
        if self.q.full():
            a_prev = self.q.get()
            self.sum += a - a_prev
        else:
            self.q.put(a)
            self.len += 1
            self.sum += a
            
        return self.sum / self.len  
