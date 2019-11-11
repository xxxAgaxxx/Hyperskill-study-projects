import random


def get_shape():
    """Asks player to enter his shape ('rock', 'paper', or 'scissors' in classic edition).
    Player could enter one of special commands, so function returns string if command not '!exit'.
    :return:players decision as string or False in case when user wants to quit the game
    """
    shape = input()
    if shape != '!exit':
        return shape
    else:
        print('Bye!')
        return False


def shape_is_correct(players_shape):
    """Gets player's shape and checks that input is correct:
    if input is one of possible shapes returns True
    else prints required information and returns False
    :param players_shape:
    :return:
    """
    if players_shape in shape_pool:
        return True
    elif players_shape in special_commands:
        if players_shape == '!help':
            print('''Please type "rock", "paper" or "scissors"
                    You win if your shape beats computer's shape:
                    Paper > rock > scissors > paper and so on''')
            return False
        if players_shape == '!rating':
            print(f'Your rating: {players_scores[player_name]}')
            return False
    else:
        print('Input incorrect! Possible shapes in this game is:', ', '.join(shape_pool))
        return False


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


shape_pool = ['rock', 'scissors', 'paper']
special_commands = ['!help', '!rating']
players_scores = dict()

try:
    rating_file = open('rating.txt')
    for line in rating_file:
        players_scores.update({line.split()[0]: int(line.split()[1])})
finally:
    rating_file.close()

player_name = input('Enter your name: ')
print(f'Hello, {player_name}')
if player_name not in players_scores.keys():
    players_scores.update({player_name: 0})
current_score = players_scores[player_name]
while True:
    players_shape = get_shape()
    if players_shape is bool and not players_shape:
        break
    if shape_is_correct(players_shape):
        computers_shape = computers_decision(shape_pool)
        winner = round_result(players_shape, computers_shape)
        if winner == 'Draw':
            current_score += 50
        if winner == 'Player':
            current_score += 100
