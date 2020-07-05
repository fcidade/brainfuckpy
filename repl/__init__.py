from brainfuck import Brainfuck

def repl(input_: str = ''):
    print("""
        ______           _        __            _                  
        | ___ \         (_)      / _|          | |                 
        | |_/ /_ __ __ _ _ _ __ | |_ _   _  ___| | __  _ __  _   _ 
        | ___ \ '__/ _` | | '_ \|  _| | | |/ __| |/ / | '_ \| | | |
        | |_/ / | | (_| | | | | | | | |_| | (__|   < _| |_) | |_| |
        \____/|_|  \__,_|_|_| |_|_|  \__,_|\___|_|\_(_) .__/ \__, |
                                                      | |     __/ |
                                                      |_|    |___/ 

        Welcome to the Brainfuck interpreter :)
        Written in Python 3 by @franciscocid (on Github!)
        Repo: https://github.com/franciscocid/brainfuckpy

    """)
    while True:
        try:
            repl_code = input('>> ')
            brain = Brainfuck()
            result = brain.run(repl_code, input_)
            print(result)
        except (EOFError, KeyboardInterrupt):
            print("...Exiting...")
            exit(0)
        except Exception as e:
            print(e)
            raise e