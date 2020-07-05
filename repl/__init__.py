from brainfuck import Brainfuck

def repl():
    while True:
        try:
            repl_code = input('> ')
            brain = Brainfuck()
            result = brain.run(repl_code)
            print(result)
        except Exception as e:
            print(e)
            raise e