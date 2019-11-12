import random


def get_shape_pool():
    """Asks player to choose game mode, a string of shapes
    separated by commas without whitespaces is expected.
    Number of shapes must be odd.
    In case when input is empty — set classic mode with 3 shapes.
    """
    global shape_pool
    shape_pool = input().split(',')
    if len(shape_pool) % 2 == 0:
        print('Number of possible variants must be odd in RSP-like games!')
        return False
    if shape_pool == ['']:
        shape_pool = ['rock', 'paper', 'scissors']
    return True



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
    if players_shape == '!help':
        print('''Please type "rock", "paper" or "scissors"
                You win if your shape beats computer's shape:
                Paper > rock > scissors > paper and so on''')
        return False
    if players_shape == '!rating':
        print(f'Your rating: {current_scores}')
        return False
    else:
        print('Input incorrect! Possible shapes in this game is:', ', '.join(shape_pool))
        return False


def computers_decision():
    """Gets all possible shapes ('rock', 'paper', or 'scissors' in classic edition) and
    returns the value randomly selected from all possible shapes.
    :param:
    :return:randomized value out of all possible
    """
    random_computers_shape = random.choice(shape_pool)
    return random_computers_shape


def round_result(player, computer, game_mode):
    """Gets two shapes as strings (two players' decisions) and resolves
     who is winner in this round. At site prints round result.

    if game_mode == 5:
        shape_pool = ['rock', 'scissors', 'lizard', 'paper', 'spock']
        rock: ['scissors', 'lizard']
        scissors: ['paper', 'lizard']
        spock: ['scissors', 'rock']
        lizard: ['paper', 'spock']
        paper: ['spock', 'rock']
    if game_mode == 15:
    shape_pool = ['rock', 'gun', 'lightning', 'devil', 'dragon',
                  'water', 'air', 'paper', 'sponge', 'wolf',
                  'tree', 'human', 'snake', 'scissors', 'fire']
    :param game_mode:Number of possible shapes
    :param player:Human player's decision
    :param computer:Computer's decision
    :return:Draw, or Player or computer as string
    """
    if player == computer:
        print(f'There is a draw ({player})')
        return 'Draw'

    first_num = shape_pool.index(computer)
    second_num = shape_pool.index(player)
    if first_num < second_num:
        if (second_num - first_num) > game_mode // 2:
            print('Sorry, but computer chose ' + computer)
            return 'Computer'
        else:
            print(f'Well done. Computer chose {computer} and failed')
            return 'Player'
    else:
        if (first_num - second_num) > game_mode // 2:
            print(f'Well done. Computer chose {computer} and failed')
            return 'Player'
        else:
            print('Sorry, but computer chose ' + computer)
            return 'Computer'


shape_pool = []
players_scores = dict()
with open('rating.txt', 'r') as rating_file:
    for line in rating_file:
        players_scores.update({line.split()[0]: int(line.split()[1])})

player_name = input('Enter your name: ')
print(f'Hello, {player_name}')
initial_scores = players_scores.get(player_name, 0)
current_scores = initial_scores

while not get_shape_pool():
    continue
print("Okay, let's start")
while True:
    players_shape = get_shape()
    if type(players_shape) is bool and not players_shape:
        break
    if shape_is_correct(players_shape):
        computers_shape = computers_decision()
        winner = round_result(players_shape, computers_shape, len(shape_pool))
        if winner == 'Draw':
            current_scores += 50
        if winner == 'Player':
            current_scores += 100

if current_scores != initial_scores:
    players_scores.update({player_name: current_scores})
with open('rating.txt', 'w') as rating_file:
    for key, value in players_scores.items():
        rating_file.write(f'{key} {value}\n')
