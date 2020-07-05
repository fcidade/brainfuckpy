from brainfuck import Brainfuck

def repl():
    while True:
        try:
            code = input('> ')
            b = Brainfuck()
            b.run(code)
        except Exception as e:
            print(e)
            raise e