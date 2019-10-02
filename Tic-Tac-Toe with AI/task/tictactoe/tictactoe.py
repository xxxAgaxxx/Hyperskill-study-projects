def initiate_field():
    field_string = input('Enter cells: ')
    cell_states = [i for i in field_string[1:10]]
    return cell_states


def show_field(field):
    print('---------')
    for i in range(3):
        print(f'| {field[3 * i]} {field[3 * i + 1]} {field[3 * i + 2]} |')
    print('---------')


current_field = initiate_field()
show_field(current_field)
