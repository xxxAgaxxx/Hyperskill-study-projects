import random


def get_shape():
    shape = input()
    return shape


def computers_decision(shapes):
    computers_shape = random.choice(shapes)
    return computers_shape


def round_result(player, computer):
    if player == computer:
        print('There is a draw ({})'.format(player))
        return 0
    elif (player == 'rock' and computer == 'paper') or (player == 'paper' and computer == 'scissors') or (player == 'scissors' and computer == 'rock'):
        print('Sorry, but computer chose ' + computer)
        return 1
    else:
        print('Well done. Computer chose {} and failed'.format(computer))
        return 'rock'


shape_pool = ['rock', 'paper', 'sciccors']
players_shape = get_shape()
computers_shape = computers_decision(shape_pool)
round_result(players_shape, computers_shape)
