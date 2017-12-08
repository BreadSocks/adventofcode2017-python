registers = dict()
highest_register_value = 0
with open("input.txt") as inputFile:
    for line in inputFile:
        parts = line.strip("\n").split()
        register = parts[0]
        command = parts[1]
        by = int(parts[2])
        condition_register = parts[4]
        condition_check = parts[5]
        condition_value = int(parts[6])

        if register not in registers:
            registers[register] = 0

        if condition_register not in registers:
            registers[condition_register] = 0

        condition_result = False
        value = registers[condition_register]
        if condition_check == ">":
            condition_result = value > condition_value
        elif condition_check == "<":
            condition_result = value < condition_value
        elif condition_check == ">=":
            condition_result = value >= condition_value
        elif condition_check == "<=":
            condition_result = value <= condition_value
        elif condition_check == "==":
            condition_result = value == condition_value
        elif condition_check == "!=":
            condition_result = value != condition_value
        else:
            print "Found new condition check : ", condition_check

        if not condition_result:
            continue

        if command == "inc":
            registers[register] += by
        elif command == "dec":
            registers[register] -= by
        else:
            print "Found new command : ", command

        highest_so_far = registers[max(registers, key=registers.get)]
        if highest_so_far > highest_register_value:
            highest_register_value = highest_so_far

print "Part 2", highest_register_value
