import random
import sqlite3


class BankError(Exception):
    """An exception class for banking system"""
    def LoginError(self):
        pass

    def FullBank(self, account):
        pass


class Bank:
    def __init__(self, bank_bin='400000'):
        self.__bank_bin = bank_bin
        self.__is_authorized = False
        # будет храниться в card.number
        self.__accounts = dict()
        self.__num_of_clients = 0
        self.__current_user = '0'
        self.__data_base = 'example.s3db'
        self.__db_connection = sqlite3.connect(self.__data_base)

    def is_logged_in(self):
        return self.__is_authorized

    def handle_user(self):
        if not self.is_logged_in():
            try:
                self.handle_unlogged()
            except BankError.LoginError:
                print('Login or password incorrect')
        else:
            self.handle_client()

    def handle_unlogged(self):
        hello_message = '1. Create an account\n2. Log into account\n0. Exit\n'
        operation = input(hello_message)
        if operation == '1':
            try:
                new_account = self.emmit_new_card()
            except BankError.FullBank():
                print('Cant create account due to bank is overhyped')
        elif operation == '2':
            try:
                self.log_in()
            except BankError.LoginError:
                raise BankError.LoginError
        elif operation == '0':
            self.__is_authorized = False
            print('Bye!')
        else:
            self.__is_authorized = False
            print('Unknown command!')

    def log_in(self):
        card_number = input('Enter your card number:\n')
        pin = input('Enter your PIN:\n')
        if self.user_is_valid(card_number, pin):
            self.__is_authorized = True
            self.__current_user = card_number
            print('You have successfully logged in!')
        else:
            raise BankError.LoginError("Wrong card number or PIN!")

    def emmit_new_card(self, card_num_len=16):
        if self.__num_of_clients >= 10 ** (card_num_len - self.__bank_bin):
            raise BankError.FullBank(f'All card numbers with card number length'
                                     f' {card_num_len} in use, try to create card'
                                     f' with larger card number length!')
        card_num = self.generate_card_number(card_num_len)
        card_pin = ''.join(map(str, [random.randint(0, 9) for _ in range(4)]))
        card_balance = 0
        self.__accounts[card_num] = {'pin': card_pin, 'balance': card_balance}
        print(f'''Your card has been created\nYour card number:\n{card_num}\nYour card PIN:\n{card_pin}''')

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

    def user_is_valid(self, card_number, pin):
        if card_number in self.__accounts:
            if pin == self.__accounts[f'{card_number}']['pin']:
                return True
        return False

    def generate_card_number(self, num_len):
        while True:
            account_identifier = ''.join(map(str, [random.randint(0, 9) for _ in range(num_len - len(self.__bank_bin) - 1)]))
            # @todo replase self.__accounts to (select number from table)
            if account_identifier not in self.__accounts:
                break
        return self.__bank_bin + account_identifier + self.checksum(account_identifier)

    def checksum(self, number_base):
        number_base = (self.__bank_bin + number_base)[::-1]
        evens = 0
        for num in number_base[0::2]:
            num = int(num) * 2
            if num > 9:
                evens += num - 9
            else:
                evens += num
        odds = sum(map(int, number_base[1::2]))
        return str((10 - (evens + odds) % 10) % 10)



if __name__ == '__main__':
    CandleFactory = Bank()
    while True:
        CandleFactory.handle_user()
