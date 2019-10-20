from string import digits


def show_field(field_in_list: list):
    """ Prints current state of the field with some cosmetics
        Input is nested lists with lines of field
    :param field_in_list: field as nested list of lines
    :return:
    """
    print('---------')
    for i in range(3):
        print(f'| {field_in_list[i][0]} {field_in_list[i][1]} {field_in_list[i][2]} |')
    print('---------')
    return


def drawn(field_in_list: list):
    """ Check that field has empty cells
    """
    if not sum(x.count(' ') for x in field_in_list):
        print('Draw')
        return True
    else:
        return False


def win_condition(field_in_list: list):
    """ Search for 3 X or O in a row on the field
    :return:
    True if one of players has 3 in a row (* wins)
    True if both players has 3 in a row (Impossible state)
    True if no one won and no empty cells remaining (Draw)
    else False (if field legit and no one won)
    """
    o_is_winner = x_is_winner = 0
    # check diagonals
    if (field_in_list[0][0] == field_in_list[1][1] == field_in_list[2][2]
            or field_in_list[2][0] == field_in_list[1][1] == field_in_list[0][2]):
        if field_in_list[1][1] == "X":
            x_is_winner = 1
        elif field_in_list[1][1] == "O":
            o_is_winner = 1
    # check rows
    for i in range(3):
        if field_in_list[i][0] == field_in_list[i][1] == field_in_list[i][2]:
            if field_in_list[i][1] == "X":
                x_is_winner = 1
            elif field_in_list[i][1] == "O":
                o_is_winner = 1
    # check columns
    for i in range(3):
        if field_in_list[0][i] == field_in_list[1][i] == field_in_list[2][i]:
            if field_in_list[1][i] == "X":
                x_is_winner = 1
            elif field_in_list[1][i] == "O":
                o_is_winner = 1
    if o_is_winner:
        if x_is_winner:
            print('Impossible')
            return True
        else:
            print('O wins')
            return True
    elif x_is_winner:
        print('X wins')
        return True
    elif drawn(field_in_list):
        return True
    return False


def coordinates_are_valid(coordinates: list):
    """Checks user enter two separate numbers in range from 1 to 3
    :param coordinates: List of coordinates
    :return: False if received more or less than 2 coordinates
    False if coordinates not numbers
    False if received coordinates less than 1 or more than 3
    """
    if len(coordinates) != 2:
        print("Please enter 2 coordinates")
        return False
    for coordinate in coordinates:
        if coordinate not in digits:
            print("You should enter numbers!")
            return False
        elif int(coordinate) < 1 or int(coordinate) > 3:
            print('Coordinates should be from 1 to 3!')
            return False
    return True


def get_step(sign: str):
    """ Asks user to enter coordinates of cell to set his sign
        Format of coordinates 'M N' where M is column from left (1) to the right (3)
                                          N is row from bottom (1) to the top (3)
        Checks that received  data is two numbers in range (1 .. 3)
        Checks that the cell at coordinates is empty and sets sign from input on the field
    :return: If player's turn accepted and field modified returns opposite players sign, else — False
    """
    cell_coordinates = input('Enter the coordinates: ').split()
    if not coordinates_are_valid(cell_coordinates):
        return False
    # forms coordinates list[x][y]
    # x — row(0..2) from left to the right, y — column(0..2) from top to bottom
    adapted_coordinates = [3 - int(cell_coordinates[1]), int(cell_coordinates[0]) - 1]
    if is_empty(adapted_coordinates, sign):
        if sign == 'X':
            return 'O'
        return 'X'
    return False


def is_empty(coordinates: list, sign: str):
    if current_field[coordinates[0]][coordinates[1]] == ' ':
        current_field[coordinates[0]][coordinates[1]] = sign
        return True
    else:
        print('This cell is occupied! Choose another one!')
        return False


current_field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
show_field(current_field)
current_player = 'X'
while True:
    next_player = get_step(current_player)
    if not next_player:
        continue
    show_field(current_field)
    if win_condition(current_field):
        break
    current_player = next_player
