from brainfuck import Brainfuck
from util.logger import setup_logs
from repl import repl
import argparse, logging

arg_parser = argparse.ArgumentParser(prog='brainfuck', description='Brainfuck VM')
arg_parser.add_argument('source', nargs='?', help='Source file')
arg_parser.add_argument('--log', action='store_true', help='Display logs on stdout')
args = arg_parser.parse_args()

if args.log:
    setup_logs()

if args.source:
    logging.info('Loading from source: ' + args.source)

    brain = Brainfuck()
    with open(args.source, 'r') as f:
        result = brain.run(f.read())
        print(result)
else:
    logging.info('Setting up REPL...')
    repl()