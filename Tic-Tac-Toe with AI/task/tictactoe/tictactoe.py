def initiate_field() -> list:
    """ Asks the user to specify the current state of the field.
        A string of 9 characters in quotes is expected to be entere.
        :rtype: list
        :return:
        Nested lists of 3 signs
    """
    field_as_string = input('Enter cells: ')
    if len(field_as_string) != 9:
        print('I wanna get string of field cell states without any other signs')
        return 0
    for sign in field_as_string:
        if sign not in 'XO_':
            print('You can use only X and O signs, and _ for whitespaces')
            return 0
    field_as_string = field_as_string.replace('_', ' ')
    cell_states = [[field_as_string[sign + 3 * i] for sign in range(0, 3)] for i in range(3)]
    if abs(field_as_string.count('X') - field_as_string.count('O')) > 1:
        show_field(cell_states)
        print("Impossible")
        return 0
    return cell_states


def show_field(field_in_list):
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
    return 1


def drawn(field_in_list):
    """ Check that field has empty cells
    """
    if not sum(x.count(' ') for x in field_in_list):
        print('Draw')
        return True
    else:
        return False


def win_condition(field_in_list):
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
    """ Asks user to enter cell to make a step, checks that its blank,
        and, if it is, sets the cell to state X, else informs user,
        that step incorrect and asks for another one
        Function modifies list with field
    :return:
    """
    while True:
        cell_coordinates = input('Enter the coordinates: ').split()
        # check if field cell with cell coordinates is empty
        # set cell with cell coordinates to 'X' and return
        # else "This cell is occupied! Choose another one!"
    pass


def is_blank(x, y):
    """ Returns True if cell with coordinates is not X or O
    """
    pass


current_field = initiate_field()
if current_field:
    show_field(current_field)
    # if win_condition(current_field):
    #     print("Game not finished")
get_step()
