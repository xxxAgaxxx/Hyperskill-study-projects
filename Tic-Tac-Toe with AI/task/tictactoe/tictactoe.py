from string import digits


def initiate_field() -> list:
    """ Asks the user to specify the current state of the field.
        A string of 9 characters in quotes is expected to be entere.
        :rtype: list
        :return: Nested lists with 3 signs each
    """
    field_as_string = input('Enter cells: ')
    if len(field_as_string) != 9:
        print('I wanna get string of 9 field cell states without any other signs')
        return 0
    for sign in field_as_string:
        if sign not in 'XO_':
            print('You can use only X and O signs, and _ for whitespaces')
            return 0
    field_as_string = field_as_string.replace('_', ' ')
    cell_states = [[field_as_string[sign + 3 * i] for sign in range(3)] for i in range(3)]
    if abs(field_as_string.count('X') - field_as_string.count('O')) > 1:
        show_field(cell_states)
        print("Impossible")
        return 0
    return cell_states


def show_field(field_in_list: list):
    pass
    """ Prints current state of the field with some cosmetics
        Input is nested lists with lines of field
    :param field: field as nested list of lines
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
    False if one of players has 3 in a row (* wins)
    False if both players has 3 in a row (Impossible state)
    False if no one won and no empty cells remaining
    else True (if field legit and no one won)
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
            # when the field has three X in a row as well as three O in a row
            print('Impossible')
            return False
        else:
            print('O wins')
            return False
    elif x_is_winner:
        print('X wins')
        return False
    elif drawn(field_in_list):
        return False
    return True


def get_step():
    """ Asks user to enter coordinates of cell to set his sing
        Format of coordinates 'M N' where M is column from left (1) to the right (3)
                                          N is row from bottom (1) to the top (3)
        Checks that received  data is two numbers in range (1 .. 3)
        Checks that the cell at coordinates is empty and sets sign 'X' on the field
    :return: True if player's turn accepted and field modified
    """
    cell_coordinates = input('Enter the coordinates: ').split()
    if len(cell_coordinates) != 2:
        print("Please enter 2 coordinates")
        return False
    for coordinate in cell_coordinates:
        if coordinate not in digits:
            print("You should enter numbers!")
            return False
        elif int(coordinate) < 1 or int(coordinate) > 3:
            print('Coordinates should be from 1 to 3!')
            return False
    # forms coordinates list[x][y]
    # x — row(0..2) from left to the right, y — column(0..2) from top to bottom
    adapted_coordinates = [3 - int(cell_coordinates[1]), int(cell_coordinates[0]) - 1]
    if is_empty(adapted_coordinates):
        return True
    return False


def is_empty(coordinates: list):
    if current_field[coordinates[0]][coordinates[1]] == ' ':
        current_field[coordinates[0]][coordinates[1]] = 'X'
        return True
    else:
        print('This cell is occupied! Choose another one!')
        return False


current_field = initiate_field()
if current_field:
    show_field(current_field)
    # if win_condition(current_field):
    #     print("Game not finished")
while not get_step():
    pass
show_field(current_field)
