import random

def players_decision():
    shape = input()
    return shape


def computers_decision(shapes):
    computers_shape = random.choice(shapes)
    return computers_shape


def round_result(player, computer):
    if player == computer:
        print('There is a draw ({})'.format(player))
        return 0
    elif (player == 'rock' and computer == 'paper') or \
            (player == 'paper' and computer == 'scissors') or \
            (player == 'scissors' and computer == 'rock'):
        print('Sorry, but computer chose ' + computer)
        return 1
    elif (player == 'paper' and computer == 'rock') or \
            (player == 'scissors' and computer == 'paper') or \
            (player == 'rock' and computer == 'scissors'):
        print('Well done. Computer chose {} and failed'.format(computer))
        return 2
    else:
        return 3


shape_pool = ['rock', 'paper', 'scissors']
while True:
    players_shape = players_decision()
    if players_shape == '!exit':
        break
    if players_shape == '!help':
        print('''Please type "rock", "paper" or "scissors"
        You win if your shape beats computer's shape:
        Paper>rock>scissors>paper and so on''')
        continue
    computers_shape = computers_decision(shape_pool)
    while round_result(players_shape,computers_shape) == '3':
        continue
print('Bye!')