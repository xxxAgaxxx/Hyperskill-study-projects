import random


class BankError(Exception):
    """An exception class for banking system"""


class Bank:
    def __init__(self, bank_bin='400000'):
        self.__bank_bin = bank_bin
        self.__is_authorized = False
        self.__accounts = dict()
        self.__current_user = '0'

    def emmit_new_card(self, card_num_len=16):
        if len(self.__accounts) > 10 ** card_num_len - 1:
            raise BankError('All card numbers are currently in use')
        card_num = self.generate_card_number(card_num_len)
        card_pin = ''.join(map(str, [random.randint(0, 9) for _ in range(4)]))
        card_balance = 0
        self.__accounts[card_num] = {'pin': card_pin, 'balance': card_balance}
        print(f'''Your card has been created\nYour card number:\n{card_num}\nYour card PIN:\n{card_pin}''')

    def is_logged_in(self):
        return True if self.__is_authorized else False

    def log_in(self):
        card_number = input('Enter your card number:\n')
        pin = input('Enter your PIN:\n')
        if self.user_is_valid(card_number, pin):
            self.__is_authorized = True
            self.__current_user = card_number
            print('You have successfully logged in!')
        else:
            print('Wrong card number or PIN!')

    def user_is_valid(self, card_number, pin):
        if card_number in self.__accounts:
            if pin == self.__accounts[f'{card_number}']['pin']:
                return True
        return False

    def generate_card_number(self, num_len):
        while True:
            account_identifier = ''.join(map(str, [random.randint(0, 9) for _ in range(num_len - len(self.__bank_bin) - 1)]))
            if account_identifier not in self.__accounts:
                break
        return self.__bank_bin + account_identifier + self.checksum()

    def checksum(self):
        return str(5)

    def handle_unlogged(self):
        hello_message = '1. Create an account\n2. Log into account\n0. Exit\n'
        operation = input(hello_message)
        if operation == '1':
            CandleFactory.emmit_new_card()
            return True
        elif operation == '2':
            CandleFactory.log_in()
            return True
        elif operation == '0':
            self.__is_authorized = False
            print('Bye!')
        else:
            self.__is_authorized = False
            print('Unknown command!')
        return False

    def handle_client(self):
        hello_message = '1. Balance\n2. Log out\n0. Exit\n'
        operation = input(hello_message)
        if operation == '1':
            print(self.__accounts[f'{self.__current_user}']['balance'])
        if operation == '2':
            self.__is_authorized = False
        if operation == '0':
            self.__is_authorized = False
            print('Bye!')
        return False


if __name__ == '__main__':
    CandleFactory = Bank()
    while True:
        if not CandleFactory.is_logged_in():
            if not CandleFactory.handle_unlogged():
                break
        else:
            if not CandleFactory.handle_client():
                break
