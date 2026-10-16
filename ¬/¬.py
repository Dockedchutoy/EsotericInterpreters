is_universe = True # Would be false if universe didn't exist

def neg(program):
    for char in program:
        if char == "¬":
            if not is_universe:
                print(42)
            else:
                print("ERR_1: Universe exists.")
                break

while True:
    neg(input(" ¬>"))