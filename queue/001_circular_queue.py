class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.k = k
        self.h, self.t = -1, -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.h = 0
        self.t = (self.t + 1) % self.k
        
        self.q[self.t] = value
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        # self.q[self.h] = None
        
        # If not last element in a queue
        if self.h != self.t:
            self.h = (self.h + 1) % self.k
        # If last element, reset the indices
        else:
            self.h, self.t = -1, -1
        
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.q[self.h]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.q[self.t]

    def isEmpty(self) -> bool:
        return self.t == -1

    def isFull(self) -> bool:
        if self.t == self.k - 1:
            return self.h == 0
        return self.h - self.t == 1
