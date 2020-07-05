from unittest import TestCase
from brainfuck import Token

class TestToken(TestCase):

    def test_token_creation(self):
        token = Token('+')
        self.assertEqual(token.type, '+')