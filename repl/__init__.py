from brainfuck import Brainfuck

def repl(input_: str = ''):
    while True:
        try:
            repl_code = input('> ')
            brain = Brainfuck()
            result = brain.run(repl_code, input_)
            print(result)
        except Exception as e:
            print(e)
            raise e