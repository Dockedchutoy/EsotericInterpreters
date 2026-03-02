import sys

def deadfish(program):
    """
    Expects a string (or a list of letters) representing Deadfish code. Returns the resulting accumulator and whether the program halted ('h' command) or not.
    """
    acc = 0
    for cmd in program:
        if cmd == "i":
            acc += 1
        elif cmd == "d":
            acc -= 1
        elif cmd == "s":
            acc *= acc
        elif cmd == "o":
            print(acc)
        elif cmd == "h":
            return acc, True
        
        if acc == -1 or acc == 256:
            acc = 0
    
    return acc, False

if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            with open(sys.argv[1]) as source:
                deadfish(source)
        except FileNotFoundError:
            print("File not found.")

    elif len(sys.argv) < 2:
        while True:
            program = input(" >")
            end_result, halted = deadfish(program)
            if halted == True:
                sys.exit()
    
    else:
        print("Either enter a single deadfish file or no arguments")