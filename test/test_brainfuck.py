from unittest import TestCase
from brainfuck import Brainfuck
import os

class TestInterpreter(TestCase):

    def setUp(self):
        self.bf = Brainfuck()

    def test_multiple_programs_and_their_outputs(self):
        cases = [
            ('print_input.b', 'hello world', 'hello world'),
            ('test.b', '', 'i\'m a test'),
        ]

        for file, args, output in cases:
            path: str = os.path.join('test', 'programs', file)
            with open(path, 'r') as code_file:
                code: str = code_file.read()
                self.assertEqual(self.bf.run(code, args), output)