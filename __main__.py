from brainfuck import Brainfuck
from util.logger import setup_logs
from repl import repl
import argparse, logging

arg_parser = argparse.ArgumentParser(prog='brainfuck', description='Brainfuck VM')
arg_parser.add_argument('source', nargs='?', help='Source file')
arg_parser.add_argument('--input', nargs='*', help='Input text')
arg_parser.add_argument('--log', action='store_true', help='Display logs on stdout')
args = arg_parser.parse_args()

if args.log:
    setup_logs()

input_: str = ' '.join(args.input)

if args.source:
    logging.info('Loading from source: ' + args.source)

    brain = Brainfuck()
    with open(args.source, 'r') as f:
        result = brain.run(f.read(), input_=input_)
        print(result)
else:
    logging.info('Setting up REPL...')
    repl(input_=input_)