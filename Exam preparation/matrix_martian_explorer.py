def rover_movement(matrix_data):

    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }

    deposits = {
        "W": 0,
        "M": 0,
        "C": 0,
    }
    rover_pos = []
    rover_directions = input().split(", ")
    for row in range(len(matrix_data)):
        for col in range(len(matrix_data)):
            if matrix_data[row][col] == "E":
                rover_pos = [row, col]

    for curr_direction in rover_directions:
        rover_pos[0] = rover_pos[0] + directions[curr_direction][0]
        rover_pos[1] = rover_pos[1] + directions[curr_direction][1]

        for pos in range(len(rover_pos)):
            if rover_pos[pos] < 0:
                rover_pos[pos] = len(matrix_data) - 1
            elif rover_pos[pos] == len(matrix_data):
                rover_pos[pos] = 0
        position = matrix_data[rover_pos[0]][rover_pos[1]]
        if position == "W":
            deposits["W"] += 1
            print(f"Water deposit found at ({rover_pos[0]}, {rover_pos[1]})")
        elif position == "M":
            deposits["M"] += 1
            print(f"Metal deposit found at ({rover_pos[0]}, {rover_pos[1]})")
        elif position == "C":
            deposits["C"] += 1
            print(f"Concrete deposit found at ({rover_pos[0]}, {rover_pos[1]})")
        elif position == "R":
            print(f"Rover got broken at ({rover_pos[0]}, {rover_pos[1]})")
            break

    if all(deposits.values()):
        print("Area suitable to start the colony.")
    else:
        print("Area not suitable to start the colony.")


def matrix_func():
    SIZE = 6

    curr_matrix = []

    for row in range(SIZE):
        row_data = input().split()
        curr_matrix.append(row_data)

    return curr_matrix


matrix = matrix_func()
rover_movement(matrix)