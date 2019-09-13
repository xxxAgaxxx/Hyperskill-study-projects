def get_shape():
    shape = input()
    return shape


def round_result(player):
    if player == 'rock':
        return 'paper'
    if player == 'paper':
        return 'scissors'
    if player == 'scissors':
        return 'rock'


players_shape = get_shape()
print('Sorry, but computer chose ' + round_result(players_shape))
