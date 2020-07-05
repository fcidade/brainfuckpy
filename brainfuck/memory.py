from typing import List

class Memory:
    def __init__(self, size: int):
        self.data = [0] * size
        self.pointer = 0

    def shift_left(self):
        self.pointer = (self.pointer - 1) % len(self.data)

    def shift_right(self):
        self.pointer = (self.pointer + 1) % len(self.data)
    
    def increment(self):
        self.data[self.pointer] += 1
        self.data[self.pointer] %= 256

    def decrement(self):
        self.data[self.pointer] -= 1
        self.data[self.pointer] %= 256

    def read(self):
        return self.data[self.pointer]

    def write(self, value: int):
        self.data[self.pointer] = value

    def __str__(self):
        return str(self.data)