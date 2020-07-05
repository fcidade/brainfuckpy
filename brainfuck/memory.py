from typing import List

class Memory:
    """
        Emulates a virtual memory
    """

    def __init__(self, size: int):
        """ @size: defines the quantity of bytes in the memory """
        self.data = [0] * size
        self.pointer = 0

    def shift_left(self):
        """
            Shifts memory pointer to the left, and wraps if overflow
        """
        self.pointer = (self.pointer - 1) % len(self.data)

    def shift_right(self):
        """
            Shifts memory pointer to the right, and wraps if overflow
        """
        self.pointer = (self.pointer + 1) % len(self.data)
    
    def increment(self):
        """
            Increments current pointing data by one and wraps between 0~255
        """
        self.data[self.pointer] += 1
        self.data[self.pointer] %= 256

    def decrement(self):
        """
            Decrements current pointing data by one and wraps between 0~255
        """
        self.data[self.pointer] -= 1
        self.data[self.pointer] %= 256

    def read(self):
        """
            Returns current pointing data
        """
        return self.data[self.pointer]

    def write(self, value: int):
        """
            Writes an integer value to the current pointing data
        """
        self.data[self.pointer] = value

    def __str__(self):

        """
            Prettify memory data as string
        """
        return str(self.data)