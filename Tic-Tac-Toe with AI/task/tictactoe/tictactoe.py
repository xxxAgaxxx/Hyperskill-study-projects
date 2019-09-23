def show_field(field):
    counter = 0
    for symbol in field:
        print(symbol, end='')
        while counter < 2:
            print(' ', end='')
            counter += 1
            break
        else:
            print('')
            counter = 0


initial_field = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

current_field = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']

show_field(current_field)