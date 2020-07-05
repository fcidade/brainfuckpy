from brainfuck import Memory
from brainfuck import Token
from typing import List
import pdb, logging

class Interpreter:
    """
        Mimic a Brainfuck "Virtual Machine"
    """
    def __init__(self):
        self.reset()

    def reset(self):
        """
            Resets all VM atributes
            Ram: Represents the VM memory
            Stdout: Output text
            Input Pointer: Current input character
            Program Counter: Current token
            Stack: Stack of loop start indexes
        """
        self.ram = Memory(256 * 10)
        self.stdout = ''
        self.input_ptr = 0
        self.pc = 0
        self.stack = []
        logging.debug('Reset all')

    def interpret(self, tokens: List[Token], input_: str = ''):
        """ Interpret a list of @tokens, optionally by a given @input_ """
        self.reset()

        while self.pc < len(tokens):
            logging.debug('PC: %d - Stack: %s' % (self.pc, ', '.join([str(x) for x in self.stack])))
            logging.debug('Current value: %d' % self.ram.read())

            token = tokens[self.pc]
            logging.debug('Token: %s' % token)
            
            self.behave(token.type)(input_)
            self.pc += 1

        return self.stdout

    def behave(self, type: str):
        """
            Handles current token behaviour
        """
        return {
            '+': lambda x: self.plus(),
            '-': lambda x: self.minus(),
            '<': lambda x: self.shift_left(),
            '>': lambda x: self.shift_right(),
            ',': lambda x: self.comma(x),
            '.': lambda x: self.dot(),
            '[': lambda x: self.left_bracket(),
            ']': lambda x: self.right_bracket(),
        }.get(type)

    def plus(self):
        """ 
            Plus(+) token behaviour:
            - Increments current pointed memory data by one
            - Wraps around 0~255
        """
        self.ram.increment()

    def minus(self):
        """ 
            Minus(-) token behaviour:
            - Decrements current pointed memory data by one
            - Wraps around 0~255
        """
        self.ram.decrement()

    def shift_left(self):
        """ 
            Shift Left(<) token behaviour:
            - Point current memory pointer to the nearest left
            - Wraps around first and last memory indexes
        """
        self.ram.shift_left()

    def shift_right(self):
        """ 
            Shift Right(>) token behaviour:
            - Point current memory pointer to the nearest right
            - Wraps around first and last memory indexes
        """
        self.ram.shift_right()

    def comma(self, input_: str):
        """ 
            Comma(,) token behaviour:
            - Writes user current character input as integer into memory
            - Increments current character input pointer by one (wraps around the input length)
            - Returns \0 if no input
        """
        if len(input_) == 0:
            self.ram.write(0)
        else:
            self.ram.write(ord(input_[self.input_ptr]))
            self.input_ptr = (self.input_ptr + 1) % len(input_)

    def dot(self):
        """ 
            Dot(.) token behaviour:
            - Prints current memory value as an ASCII character
        """
        self.stdout += chr(self.ram.read())

    def left_bracket(self):
        """ 
            Left Bracket([) token behaviour:
            - Start loop
            - Append current program counter to the stack
        """
        self.stack.append(self.pc)

    def right_bracket(self):
        """ 
            Right Bracket([) token behaviour:
            - Check if current memory value is equal to zero
            - If true:
                - Pops the stack and continues to the next token
            - Otherwise:
                - Loops back to the stack top address
        """
        if self.ram.read() == 0:
            self.stack.pop()
        else:
            self.pc = self.stack[-1]