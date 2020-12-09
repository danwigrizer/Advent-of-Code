import logging
logging.getLogger().setLevel(logging.INFO)


def run(instructions):
    lines = 0
    accumalator = 0
    prev_value = set()
    while lines < len(instructions):
        if lines in prev_value:
            return None

        # add lines weve seen
        prev_value.add(lines)
        inst, value = instructions[lines]
        if inst == "acc":
            accumalator += value
            lines += 1
        elif inst == "jmp":
            lines += value
        else:
            lines += 1
    return accumalator


def main():
    fin = open("AoC-08-Input.txt", "r")
    prog = [line.strip().split() for line in fin.readlines() if line.strip()]
    # logging.info(f'{prog}')
    instructions = [(inst, int(x)) for inst,x in prog]
    # logging.info(f'{prog}')

    for i in range(len(instructions)):
        if instructions[i][0] == "acc":
            # logging.info(f'{prog}')
            continue
        new_inst = "jmp" if instructions[i][0] == "nop" else "nop"
        ## Putting the JMP back into the list by splitting the list
        new_inst = instructions[:i] + [(new_inst, instructions[i][1])] + instructions[i+1:]
        x = run(new_inst)
        if x is not None:
            print(x)

if __name__ == '__main__':
    main()