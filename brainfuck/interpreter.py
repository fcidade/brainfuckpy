from brainfuck import Memory
from brainfuck import Token
from typing import List
import pdb, logging

class Interpreter:
    def __init__(self):
        self.reset()

    def reset(self):
        self.ram = Memory(10)
        self.stdout = ''
        self.input_ptr = 0
        self.pc = 0
        self.stack = []
        logging.debug('Reset all')

    def interpret(self, tokens: List[Token], input_: str = ''):
        self.reset()

        while self.pc < len(tokens):
            logging.debug('PC: %d - Stack: %s' % (self.pc, ', '.join([str(x) for x in self.stack])))
            logging.debug('Current value: %d' % self.ram.read())

            token = tokens[self.pc]
            logging.debug('Token: %s' % token)
            
            self.behave(token.type)(input_)
            self.pc += 1
            #import time
            #time.sleep(1)

        return self.stdout

    def behave(self, type: str):
        fn = {
            '+': lambda x: self.plus(),
            '-': lambda x: self.minus(),
            '<': lambda x: self.shift_left(),
            '>': lambda x: self.shift_right(),
            ',': lambda x: self.comma(x),
            '.': lambda x: self.dot(),
            '[': lambda x: self.left_bracket(),
            ']': lambda x: self.right_bracket(),
        }.get(type)
        return fn

    def plus(self):
        self.ram.increment()

    def minus(self):
        self.ram.decrement()

    def shift_left(self):
        self.ram.shift_left()

    def shift_right(self):
        self.ram.shift_right()

    def comma(self, input_: str):
        if len(input_) == 0:
            self.ram.write(0)
        else:
            self.ram.write(ord(input_[self.input_ptr]))
            self.input_ptr = (self.input_ptr + 1) % len(input_)

    def dot(self):
        self.stdout += chr(self.ram.read())

    def left_bracket(self):
        self.stack.append(self.pc)

    def right_bracket(self):
        if self.ram.read() == 0:
            self.stack.pop()
        else:
            self.pc = self.stack[-1]