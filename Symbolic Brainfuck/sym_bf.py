import sys


def sym_bf(program):
    """
    Expects a string (or a list of letters) representing Symbolic Brainfuck code.
    """
    # Registers
    reg = {
        "α": 0,
        "ß": 0,
        "π": 0,
        "σ": 0,
        "µ": 0,
        "δ": 0,
        "φ": 0,
        "ε": 0,
    }

    cur = 0
    tape = [0]
    pointer = 0
    parents = []

    def swap(cmd):
        tmp = tape[pointer]
        tape[pointer] = reg[cmd]
        reg[cmd] = tmp
        del tmp

    while cur < len(program):
        match program[cur]:
            # Classic Brainfuck
            case "→":
                pointer += 1
                if pointer + 1 > len(tape): tape.append(0)  # Dynamic tape makes it basically infinite but might be slower idk will it even work?
            case "←":
                if pointer != 0: pointer -= 1
            case "▲":
                tape[pointer] += 1
            case "▼":
                if tape[pointer] != 0: tape[pointer] -= 1
            case "¡":
                print(chr(tape[pointer]))
            case "¿":
                tape[pointer] = ord(input("¿ ")[0])
            case "≤":  # This could be made better 100% but idk or care why
                if tape[pointer] < 1:
                    cur += 1
                    parents_count = 1
                    while parents_count > 0:
                        if program[cur] == "≤":
                            parents_count += 1
                        elif program[cur] == "≥":
                            parents_count -= 1
                        cur += 1
                    continue
                else:
                    parents.append(cur)
            case "≥":
                if parents != []:
                    cur = parents.pop() - 1  # Check later
                else:
                    print("Error: Missing ≤ in program")
                    return
            
            # Symbolic Brainfuck
            case "²":
                tape[pointer] *= 2
            case "½":
                tape[pointer] //= 2
            case "↨":
                tape[pointer] = pointer
            case "⌂":
                pointer = tape[pointer]

            case "α":  # I will fix this later i swear
                swap("α")
            case "ß":
                swap("ß")
            case "π":
                swap("π")
            case "σ":
                swap("σ")
            case "µ":
                swap("µ")
            case "δ":
                swap("δ")
            case "φ":
                swap("φ")
            case "ε":
                swap("ε")

        cur += 1


if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            with open(sys.argv[1]) as source:
                sym_bf(source)
        except FileNotFoundError:
            print("File not found.")

    elif len(sys.argv) < 2:
        while True:
            program = input(" >")
            sym_bf(program)
    
    else:
        print("Either enter a single Symbolic Brainfuck file or no arguments")