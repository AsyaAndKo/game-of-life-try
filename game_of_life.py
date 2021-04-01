with open("entry.txt", "r") as f:
    gen_num = int(f.readline())
    field_size = [int(i) for i in f.readline().split(" ")
                  ]  # 1 argument = y, 2 argument = x
    first_gen = [[j for j in i.rstrip("\n")] for i in f.readlines()]


def new_cell_state(field_state: list, cell_x: int, cell_y: int) -> str:
    # Coordinates which are NOT placed on borders
    if (cell_x > 0 and cell_x < (field_size[1]-1)) and (cell_y > 0 and cell_y < (field_size[0]-1)):
        cells_neighbours = [
            field_state[cell_x-1][cell_y-1],
            field_state[cell_x-1][cell_y],
            field_state[cell_x-1][cell_y+1],

            field_state[cell_x][cell_y-1],
            field_state[cell_x][cell_y+1],

            field_state[cell_x+1][cell_y-1],
            field_state[cell_x+1][cell_y],
            field_state[cell_x+1][cell_y+1]
        ]
    # left top corner
    elif cell_x == 0 and cell_y == 0:
        cells_neighbours = [
            field_state[field_size[1]-1][field_size[0]-1],
            field_state[field_size[1]-1][cell_y],
            field_state[field_size[1]-1][cell_y+1],

            field_state[cell_x][field_size[0]-1],
            field_state[cell_x][cell_y+1],

            field_state[cell_x+1][field_size[0]-1],
            field_state[cell_x+1][cell_y],
            field_state[cell_x+1][cell_y+1]
        ]
    # right top corner
    elif cell_x == 0 and cell_y == field_size[0]-1:
        cells_neighbours = [
            field_state[(field_size[1]-1)-1][cell_y-1],
            field_state[field_size[1]-1][cell_y],
            field_state[field_size[1]-1][0],

            field_state[cell_x][field_size[0]-1],
            field_state[cell_x][0],

            field_state[cell_x+1][cell_y-1],
            field_state[cell_x+1][cell_y],
            field_state[cell_x+1][0]
        ]
    # top border
    elif cell_x == 0:
        cells_neighbours = [
            field_state[field_size[1]-1][cell_y-1],
            field_state[field_size[1]-1][cell_y],
            field_state[field_size[1]-1][cell_y+1],

            field_state[cell_x][cell_y-1],
            field_state[cell_x][cell_y+1],

            field_state[cell_x+1][cell_y-1],
            field_state[cell_x+1][cell_y],
            field_state[cell_x+1][cell_y+1]
        ]
    # left border
    elif cell_y == 0:
        cells_neighbours = [
            field_state[cell_x-1][field_size[0]-1],
            field_state[cell_x-1][cell_y],
            field_state[cell_x-1][cell_y+1],

            field_state[cell_x][field_size[0]-1],
            field_state[cell_x][cell_y+1],

            field_state[field_size[1]-1][field_size[0]-1],
            field_state[field_size[1]-1][cell_y],
            field_state[field_size[1]-1][cell_y+1]
        ]
    # left bottom corner
    elif cell_x == field_size[1]-1 and cell_y == 0:
        cells_neighbours = [
            field_state[cell_x-1][field_size[0]-1],
            field_state[cell_x-1][cell_y],
            field_state[cell_x-1][cell_y+1],

            field_state[cell_x][field_size[0]-1],
            field_state[cell_x][cell_y+1],

            field_state[cell_x+1][field_size[0]-1],
            field_state[cell_x+1][cell_y],
            field_state[cell_x+1][cell_y+1]
        ]
    # right bottom corner
    elif cell_x == field_size[1]-1 and cell_y == field_size[0]-1:
        cells_neighbours = [
            field_state[cell_x-1][cell_y-1],
            field_state[cell_x-1][cell_y],
            field_state[cell_x-1][0],

            field_state[cell_x][cell_y-1],
            field_state[cell_x][0],

            field_state[0][cell_y-1],
            field_state[0][cell_y],
            field_state[0][0]
        ]
    # bottom border
    elif cell_x == field_size[1]-1:
        cells_neighbours = [
            field_state[cell_x-1][cell_y-1],
            field_state[cell_x-1][cell_y],
            field_state[cell_x-1][cell_y+1],

            field_state[cell_x][cell_y-1],
            field_state[cell_x][cell_y+1],

            field_state[0][cell_y-1],
            field_state[0][cell_y],
            field_state[0][cell_y+1]
        ]
    # right border
    elif cell_y == field_size[0]-1:
        cells_neighbours = [
            field_state[cell_x-1][cell_y-1],
            field_state[cell_x-1][cell_y],
            field_state[cell_x-1][0],

            field_state[cell_x][cell_y-1],
            field_state[cell_x][0],

            field_state[cell_x+1][cell_y-1],
            field_state[cell_x+1][cell_y],
            field_state[cell_x+1][0]
        ]

    count = 0
    for i in cells_neighbours:
        if i == "x":
            count += 1
        else:
            continue
    if field_state[cell_x][cell_y] == "." and count == 3:
        field_state[cell_x][cell_y] = "x"
    elif (count in [2, 3]) and field_state[cell_x][cell_y] == "x":
        field_state[cell_x][cell_y] = "x"
    elif (count < 2 or count > 3) and field_state[cell_x][cell_y] == "x":
        field_state[cell_x][cell_y] = "."
    else:
        field_state[cell_x][cell_y] = "."
    return field_state[cell_x][cell_y]


def new_field_state(current_field_state: list) -> list:
    new_field = [["." for i in range(len(current_field_state[j]))]
                 for j in range(len(current_field_state))]
    for y in range(len(current_field_state)):
        for x in range(len(current_field_state[y])):
            new_field[y][x] = new_cell_state(current_field_state, y, x)
    return new_field


def game_of_life(current_field_state: list, number_of_generations: int) -> list:
    for i in range(number_of_generations):
        current_field_state = new_field_state(current_field_state)
        for j in current_field_state:
            print(j)
        print('\n')
    return current_field_state


if __name__ == "__main__":
    output_list = game_of_life(first_gen, gen_num)
    with open("output.txt", "w") as output:
        for item in output_list:
            output.write("%s\n" % ''.join(item))
