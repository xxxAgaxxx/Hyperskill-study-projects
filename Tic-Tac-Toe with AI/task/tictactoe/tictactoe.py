def show_field(field):
    counter = 0
    for row in field:
        print(row)


initial_field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

current_field = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]

show_field(current_field)