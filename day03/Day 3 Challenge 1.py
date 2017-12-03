count = 3

max = 23

grid = {"0,0": 1, "1,0": 2}

new_position = [1, 1]

direction_taken = "N"

while count < 347992:
    # put new info in
    grid[str(new_position[0]) + "," + str(new_position[1])] = count
    number_to_left = str(new_position[0] - 1) + "," + str(new_position[1])
    number_to_top = str(new_position[0]) + "," + str(new_position[1] + 1)
    number_to_right = str(new_position[0] + 1) + "," + str(new_position[1])
    number_to_bottom = str(new_position[0]) + "," + str(new_position[1] - 1)

    # work out next round
    if direction_taken == "N" and not grid.__contains__(number_to_left):
        direction_taken = "W"
        new_position = [new_position[0] - 1, new_position[1]]
    elif direction_taken == "E" and not grid.__contains__(number_to_top):
        direction_taken = "N"
        new_position = [new_position[0], new_position[1] + 1]
    elif direction_taken == "S" and not grid.__contains__(number_to_right):
        direction_taken = "E"
        new_position = [new_position[0] + 1, new_position[1]]
    elif direction_taken == "W" and not grid.__contains__(number_to_bottom):
        direction_taken = "S"
        new_position = [new_position[0], new_position[1] - 1]
    else:
        if direction_taken == "N":
            new_position = [new_position[0], new_position[1] + 1]
        elif direction_taken == "E":
            new_position = [new_position[0] + 1, new_position[1]]
        elif direction_taken == "S":
            new_position = [new_position[0], new_position[1] - 1]
        elif direction_taken == "W":
            new_position = [new_position[0] - 1, new_position[1]]
    count += 1

print grid

for key, value in grid.items():
    #  Example outputs
    if value == 1:
        print "Found 1 at ", key, abs(int(key.split(",")[0])) + abs(int(key.split(",")[1]))
    elif value == 12:
        print "Found 12 at ", key, abs(int(key.split(",")[0])) + abs(int(key.split(",")[1]))
    elif value == 23:
        print "Found 23 at", key, abs(int(key.split(",")[0])) + abs(int(key.split(",")[1]))
    elif value == 1024:
        print "Found 1024 at ", key, abs(int(key.split(",")[0])) + abs(int(key.split(",")[1]))
    #  answer
    elif value == 347991:
        print "Found 347991 at ", key, abs(int(key.split(",")[0])) + abs(int(key.split(",")[1]))
