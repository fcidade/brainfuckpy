from brainfuck import Token
from typing import List
import re

class Parser:
    def parse(self, code: str) -> List[Token]:
        tokens: List[Token] = []

        """ Remove unused characters """
        code = re.sub(r'[^\+\-\>\<\[\]\,\.]', '', code)

        for char in code:
            tokens.append(Token(char))

        return tokens