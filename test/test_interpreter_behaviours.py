from unittest import TestCase
from brainfuck import Interpreter

class TestInterpreterBehaviours(TestCase):
    """
        * Some Memory related behaviours wont be tested as there are already tests
        for them on test_memory.py *
    """

    def setUp(self):
        self.interpreter = Interpreter()

    def test_comma_wraps(self):
        data = [
            ('r', 1),
            ('e', 2),
            ('a', 3),
            ('d', 0),
            ('r', 1),
        ]
        self.assertEqual(self.interpreter.input_ptr, 0)
        for letter, index in data:
            self.interpreter.comma('read')
            self.assertEqual(self.interpreter.ram.read(), ord(letter))
            self.assertEqual(self.interpreter.input_ptr, index)

    def test_append_current_pc_to_the_stack(self):
        self.interpreter.left_bracket()
        self.assertEqual(self.interpreter.stack, [0])
        self.interpreter.pc += 10
        self.interpreter.left_bracket()
        self.assertEqual(self.interpreter.stack, [0, 10])

    def test_pop_stack_if_current_memory_value_evaluates_to_zero(self):
        self.interpreter.left_bracket()
        self.assertEqual(self.interpreter.stack, [0])

        self.assertEqual(self.interpreter.ram.read(), 0)

        self.interpreter.right_bracket()
        self.assertEqual(self.interpreter.stack, [])

    def test_loops_back_to_the_nearest_left_bracket_when_hit_right_bracket_token(self):
        self.interpreter.left_bracket()
        self.assertEqual(self.interpreter.stack, [0])
        self.interpreter.pc += 10
        self.interpreter.left_bracket()
        self.assertEqual(self.interpreter.stack, [0, 10])

        self.interpreter.right_bracket()
        self.assertEqual(self.interpreter.stack, [0])
        self.assertEqual(self.interpreter.pc, 10)

        self.interpreter.ram.write(2)

        self.interpreter.right_bracket()
        self.assertEqual(self.interpreter.stack, [0])
        self.assertEqual(self.interpreter.pc, 0)


        self.interpreter.minus()
        self.interpreter.right_bracket()
        self.assertEqual(self.interpreter.stack, [0])
        self.assertEqual(self.interpreter.pc, 0)

        self.interpreter.minus()
        self.interpreter.right_bracket()
        self.assertEqual(self.interpreter.stack, [])
        self.assertEqual(self.interpreter.pc, 0)