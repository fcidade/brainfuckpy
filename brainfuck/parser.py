from brainfuck import Token
from typing import List
import re

class Parser:
    """
        Removes invalid characters and convert input string into Tokens
    """

    def parse(self, code: str) -> List[Token]:
        """ Converts string of code into a list of Tokens """
        tokens: List[Token] = []

        code = self.remove_invalid_characters(code)

        for char in code:
            tokens.append(Token(char))

        return tokens

    def remove_invalid_characters(self, code: str):
        """ Remove unused characters """
        return re.sub(r'[^\+\-\>\<\[\]\,\.]', '', code)