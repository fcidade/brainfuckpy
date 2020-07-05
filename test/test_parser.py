from unittest import TestCase
from brainfuck import Parser, Token

class TestParser(TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_parser_ignores_invalid_characters(self):
        chars = self.parser.remove_invalid_characters('+-,.<>[]abcdefghijklmno+-,.<>[]pqrstuvwxyz+-,.<>[]0123456789^!@#$%*()')
        self.assertIsInstance(chars, str)
        self.assertEqual(chars, '+-,.<>[]+-,.<>[]+-,.<>[]')

    def test_parser_returns_list_of_token(self):
        self.assertIsInstance(self.parser.parse('+-,.<>[]'), list)

    def test_parser_correctly_converts_tokens(self):
        self.assertEqual(
            [x.type for x in self.parser.parse('+')],
            [Token('+').type]
        )
        self.assertEqual(
            [x.type for x in self.parser.parse('-+<>[],.')],
            [
                Token('-').type,
                Token('+').type,
                Token('<').type,
                Token('>').type,
                Token('[').type,
                Token(']').type,
                Token(',').type,
                Token('.').type,
            ]
        )