from random import choice

class ChatBot:
    bot_name = 'Useless dniwe'
    birth_year = 2007

    def __init__(self):
        self.user_name = 'Nemo'
        self.age_reminder = []
        self.user_age = 0
        self.geo_tests = [{'Question': 'What is (de jure) the capital of Switzerland?',
                           'Choices': ['1. Bern', '2. Zurich', '3. Geneva', '4. None'],
                           'Right answer': '4'},
                          {'Question': 'What is the capital of Australia?',
                           'Choices': ['1. Sydney', '2. Canberra', '3. Adelaide', '4. Melbourne'],
                           'Right answer': '2'}
                          ]

    def greeting(self):
        self.user_name = input('Please, remind me your name.\n')
        print(f'What a great name you have, {self.user_name}!')

    def guess_age(self):
        print('Let me guess your age.')
        print('Enter remainders of dividing your age by 3, 5 and 7.')
        self.age_reminder = [int(input()) for i in range(3)]
        self.user_age = (self.age_reminder[0] * 70 +
                         self.age_reminder[1] * 21 +
                         self.age_reminder[2] * 15) % 105

    def counter(self):
        print('Now I will prove to you that I can count to any number you want.')
        [print(f'{i} !') for i in range(int(input()) + 1)]

    def geography_test(self):
        print("Let's test your knowledge in geography.")
        test = choice(self.geo_tests)
        print(test['Question'])
        [print(test['Choices'][i]) for i in range(len(test['Choices']))]
        while True:
            if input() != test['Right answer']:
                print('Please, try again.')
            else:
                break
        print('Congratulations, have a nice day!')


new_bot = ChatBot()
print(f'Hello! My name is {new_bot.bot_name}.')
print(f'I was created in {new_bot.birth_year}.')
new_bot.greeting()
new_bot.guess_age()
print(f"Your age is {new_bot.user_age}; that's a good time to start programming!")
new_bot.counter()
new_bot.geography_test()
