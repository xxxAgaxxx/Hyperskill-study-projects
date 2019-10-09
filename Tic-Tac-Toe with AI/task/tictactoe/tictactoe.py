def initiate_field() -> list:
    """ Asks the user to specify the current state of the field.
        A string of 9 characters in quotes is expected to be entere.
        :rtype: list
        :return:
        Nested lists of 3 signs
    """
    field_as_string = input('Enter cells: ')
    if len(field_as_string) != 11:
        print('I wanna get string of field cell states inside "quotes"')
        return 0
    print(field_as_string.count('X'))   # !!!дебажная хуйня!!!
    print(field_as_string.count('O'))
    cell_states = [[field_as_string[sign + 3 * i] for sign in range(1, 4)] for i in range(3)]
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


def win_condition(field_in_list):
    o_is_winner, x_is_winner = 0
    if (field_in_list[0][0] == field_in_list[1][1] == field_in_list[2][2]
            or field_in_list[2][0] == field_in_list[1][1] == field_in_list[0][2]):
        if field_in_list[1][1] == "X":
            x_is_winner = 1
        elif field_in_list[1][1] == "O":
            o_is_winner = 1



current_field = initiate_field()
if current_field:
    show_field(current_field)

