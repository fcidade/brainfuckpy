from unittest import TestCase
from brainfuck import Brainfuck
import os

class TestInterpreter(TestCase):

    def setUp(self):
        self.bf = Brainfuck()

    def test_multiple_programs_and_their_outputs(self):
        with open('test/res/lorem_ipsun.txt', 'r') as f:
            lorem_ipsun = f.read()
        cases = [
            ('print_input.b', 'hello world', 'hello world'),
            ('test.b', '', 'i\'m a test'),
            ('not_really_long.b', '', 'Well, that\'s a really and really long and massive bit of text, well, not much actually, but it\'s a nice way to see if things are going as they should.'),
            ('lorem_ipsun.b', '', lorem_ipsun),
        ]

        for file, args, output in cases:
            path: str = os.path.join('test', 'programs', file)
            with open(path, 'r') as code_file:
                code: str = code_file.read()
                self.assertEqual(self.bf.run(code, args), output)