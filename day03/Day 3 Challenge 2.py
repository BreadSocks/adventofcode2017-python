count = 2

square = 3

grid = {"0,0": 1, "1,0": 1}
squares = {1: 1, 2: 1, 3: 2}

new_position = [1, 1]

direction_taken = "N"

while count < 347992:
    # put new info in
    grid[str(new_position[0]) + "," + str(new_position[1])] = count
    number_to_left = str(new_position[0] - 1) + "," + str(new_position[1])
    number_to_top = str(new_position[0]) + "," + str(new_position[1] + 1)
    number_to_right = str(new_position[0] + 1) + "," + str(new_position[1])
    number_to_bottom = str(new_position[0]) + "," + str(new_position[1] - 1)

    # work out next position
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

    # work out next count
    above = str(new_position[0]) + "," + str(new_position[1] + 1)
    above_left = str(new_position[0] - 1) + "," + str(new_position[1] + 1)
    above_right = str(new_position[0] + 1) + "," + str(new_position[1] + 1)
    middle_left = str(new_position[0] - 1) + "," + str(new_position[1])
    middle_right = str(new_position[0] + 1) + "," + str(new_position[1])
    below = str(new_position[0]) + "," + str(new_position[1] - 1)
    below_left = str(new_position[0] - 1) + "," + str(new_position[1] - 1)
    below_right = str(new_position[0] + 1) + "," + str(new_position[1] - 1)

    count = 0
    if grid.__contains__(above_left):
        count += grid[above_left]
    if grid.__contains__(above):
        count += grid[above]
    if grid.__contains__(above_right):
        count += grid[above_right]
    if grid.__contains__(middle_left):
        count += grid[middle_left]
    if grid.__contains__(middle_right):
        count += grid[middle_right]
    if grid.__contains__(below_left):
        count += grid[below_left]
    if grid.__contains__(below):
        count += grid[below]
    if grid.__contains__(below_right):
        count += grid[below_right]

    square += 1
    squares[square] = count

print grid
print squares
print squares[square]
