registers = dict()
last_played_sound = -1
recovered = []
lines = open("input.txt").read().strip().split("\n")
line_number = 0


def is_an_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


while -1 < line_number < len(lines) and len(recovered) == 0:
    parts = lines[line_number].split(" ")
    instruction = parts[0]
    register = parts[1]
    by_value = parts[2] if len(parts) > 2 else None
    jumped = False

    if register not in registers:
        registers[register] = 0

    if instruction == "set":
        registers[register] = int(by_value) if is_an_int(by_value) else registers[by_value]
    elif instruction == "add":
        registers[register] = registers[register] + int(by_value)
    elif instruction == "mul":
        multiply_by = int(by_value) if is_an_int(by_value) else registers[by_value]
        registers[register] = registers[register] * multiply_by
    elif instruction == "mod":
        registers[register] = registers[register] % (int(by_value) if is_an_int(by_value) else registers[by_value])
    elif instruction == "snd":
        last_played_sound = registers[register]
        print "Playing ", registers[register]
    elif instruction == "rcv":
        if registers[register] > 0:
            recovered.append(registers[register])
            print "Recovering sound ", last_played_sound
    elif instruction == "jgz":
        if registers[register] > 0:
            if is_an_int(by_value):
                line_number += int(by_value)
            else:
                line_number += registers[by_value]
            # line_number += int(by_value) if is_an_int(by_value) else registers[by_value]
            jumped = True

    if not jumped:
        line_number += 1

print registers
