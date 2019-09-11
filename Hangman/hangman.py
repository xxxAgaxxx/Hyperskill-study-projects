import random


def start_game(words):
    print('H A N G M A N')
    return random.choice(words)


def get_letter():
    user_input = input('Input a letter: ')
    if len(user_input) > 1:
        print('You should print a single letter')
        return 0
    if not user_input.islower():
        print('It is not an ASCII lowercase letter')
        return 0
    return user_input

def check_letter(letter):
    if letter in word_of_the_game:
        for i in range(len(word_of_the_game)):
            if letter == word_of_the_game[i]:
                current_word[i] = letter
        return current_word
    else:
        print('No such letter in the word')
        return 0


word_pool = ['python', 'java', 'kotlin', 'javascript']
word_of_the_game = start_game(word_pool)
current_word = list('-' * len(word_of_the_game))
used_letters = []
attempts_limit = 8
attempts_counter = 0
while attempts_counter < attempts_limit:
    print('\n' + ''.join(current_word))
    new_letter = get_letter()
    if new_letter == 0:
        continue
    elif new_letter in used_letters:      # была такая буква
        print('You already typed this letter')
        continue
    else:
        used_letters.append(new_letter)
    if not check_letter(new_letter):    # ошибка
        attempts_counter += 1
        continue
    if current_word == word_of_the_game:
        print('You guessed the word' + word_of_the_game + '!')
        break
else:
    print('You are hanged!')
