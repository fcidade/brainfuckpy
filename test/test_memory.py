from unittest import TestCase
from brainfuck import Memory

class TestMemory(TestCase):

    def setUp(self):
        self.memory = Memory(1024)

    def test_memory_creation(self):
        memory = Memory(10)
        self.assertEqual(len(memory.data), 10)

        memory = Memory(128)
        self.assertEqual(len(memory.data), 128)

        memory = Memory(1024)
        self.assertEqual(len(memory.data), 1024)
        
    def test_memory_starts_with_zeroes(self):
        memory = Memory(1024)
        for i in memory.data:
            self.assertEqual(i, 0)

    def test_pointer_points_to_the_first_index(self):
        self.assertEqual(self.memory.pointer, 0)

    def test_shift_to_right(self):
        self.assertEqual(self.memory.pointer, 0)
        self.memory.shift_right()        
        self.assertEqual(self.memory.pointer, 1)

    def test_shift_to_right_wraps_to_zero(self):
        self.assertEqual(self.memory.pointer, 0)
        for i in range(len(self.memory.data)):
            self.memory.shift_right()
        self.assertEqual(self.memory.pointer, 0)

    def test_shift_to_left(self):
        self.assertEqual(self.memory.pointer, 0)
        self.memory.shift_right()
        self.memory.shift_right()
        self.memory.shift_left()
        self.assertEqual(self.memory.pointer, 1)

    def test_shift_to_left_wraps_to_length(self):
        self.assertEqual(self.memory.pointer, 0)
        for i in range(len(self.memory.data)):
            self.memory.shift_left()
        self.assertEqual(self.memory.pointer, 0)

    def test_increment_by_one(self):
        self.assertEqual(self.memory.data[self.memory.pointer], 0)
        self.memory.increment()
        self.assertEqual(self.memory.data[self.memory.pointer], 1)

    def test_increment_by_one_and_wraps_between_0_and_255(self):
        self.assertEqual(self.memory.data[self.memory.pointer], 0)
        for i in range(256):
            self.memory.increment()
        self.assertEqual(self.memory.data[self.memory.pointer], 0)

    def test_decrement_by_one(self):
        self.assertEqual(self.memory.data[self.memory.pointer], 0)
        self.memory.decrement()
        self.assertEqual(self.memory.data[self.memory.pointer], 255)

    def test_decrement_by_one_and_wraps_between_0_and_255(self):
        self.assertEqual(self.memory.data[self.memory.pointer], 0)
        for i in range(256):
            self.memory.decrement()
        self.assertEqual(self.memory.data[self.memory.pointer], 0)

    def test_read_returns_a_valid_data_value(self):
        value = self.memory.read()
        self.assertIsInstance(value, int)
        self.assertEqual(value, 0)

    def test_writes_valid_value_to_memory(self):
        self.assertEqual(self.memory.read(), 0)
        self.memory.write(10)

        value = self.memory.read()
        self.assertIsInstance(value, int)
        self.assertEqual(value, 10)