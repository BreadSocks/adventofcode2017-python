registers = dict()
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
print registers

winning_register = max(registers, key=registers.get)
print "Register with highest value :", winning_register, "with :", registers[winning_register]
