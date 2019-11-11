import random


def get_shape():
    """Asks player to enter his shape ('rock', 'paper', or 'scissors' in classic edition).
    Player could enter '!exit' to quit the game, so function returns string.
    :return:players decision as string or True in case when user need '!help'
    """
    shape = input()
    check_result = check_shape(shape)
    if check_result == 1:
        return shape
    elif check_result == 2:
        return False
    elif check_result == 3:
        # print('''Please type "rock", "paper" or "scissors"
        #             You win if your shape beats computer's shape:
        #             Paper > rock > scissors > paper and so on''')
        return True
    else:
        return True


def check_shape(shape):
    """Gets player's shape and checks that input is correct:
    if input is one of possible shapes returns 1
    if input ask for !help returns 2
    if input wants to !exit out of program returns 3
        if input is something unexpected returns 4
    :param shape:
    :return:
    """
    if shape in shape_pool:
        return 1
    if shape not in special_commands:
        print('Sorry, unknown command. Possible special commands are:' + shape_pool)
        return 4
    if shape == '!help':
        print('''Please type "rock", "paper" or "scissors"
            You win if your shape beats computer's shape:
            Paper > rock > scissors > paper and so on''')
        return 2
    if shape == '!exit':
        print('Bye!')
        return 3


def computers_decision(shapes):
    """Gets all possible shapes ('rock', 'paper', or 'scissors' in classic edition) and
    returns the value randomly selected from all possible shapes.
    :param shapes:list of possible shapes
    :return:randomized value out of all possible
    """
    random_computers_shape = random.choice(shapes)
    return random_computers_shape


def round_result(player, computer):
    """Gets two shapes as strings (two players' decisions) and resolves
     who is winner in this round. At site prints round result.

    :param player:Human player's decision
    :param computer:Computer's decision
    :return:Draw, or Player or computer as string
    """
    if player == computer:
        print(f'There is a draw ({player})')
        return 'Draw'
    elif (player == 'rock' and computer == 'paper') or \
         (player == 'paper' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'rock'):
        print('Sorry, but computer chose ' + computer)
        return 'Player'
    else:
        print(f'Well done. Computer chose {computer} and failed')
        return 'Computer'


shape_pool = ['rock', 'paper', 'scissors']
special_commands = ['!exit', '!help', '!rating']
players_scores = dict()

try:
    rating_file = open('rating.txt')
    for line in rating_file:
        players_scores.update({line.split()[0]: line.split()[1]})
finally:
    rating_file.close()

player_name = input('Enter your name: ')
print(f'Hello, {player_name}')

while True:
    players_shape = get_shape()
    if players_shape:
        if players_shape not in shape_pool:
            print('Input incorrect! Possible shapes in this game is:', ', '.join(shape_pool))
            continue
        computers_shape = computers_decision(shape_pool)
        # print(computers_shape)
        round_result(players_shape, computers_shape)
    else:
        break
