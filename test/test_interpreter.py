from unittest import TestCase
from brainfuck import Interpreter, Parser

class TestInterpreter(TestCase):

    def setUp(self):
        self.parser = Parser()
        self.interpreter = Interpreter()

    def test_interpreter_resets_all_properties(self):
        self.interpreter.reset()
        
        self.assertEqual(self.interpreter.ram.data, [0] * 256 * 10)
        self.assertEqual(self.interpreter.stdout, '')
        self.assertEqual(self.interpreter.input_ptr, 0)
        self.assertEqual(self.interpreter.pc, 0)
        self.assertEqual(self.interpreter.stack, [])

    def test_outputs_hello_world(self):
        hello_world = '-[------->+<]>-.-[->+++++<]>++.+++++++..+++.[--->+<]>-----.---[->+++<]>.-[--->+<]>---.+++.------.--------.'
        parsed = self.parser.parse(hello_world)
        self.interpreter.interpret(parsed)
        self.assertEqual(self.interpreter.stdout, 'Hello World')