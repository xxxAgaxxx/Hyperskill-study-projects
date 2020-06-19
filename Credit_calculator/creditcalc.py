import argparse
import math


def arguments_correct(credit):
    try:
        credit.interest = float(credit.interest)
    except ValueError:
        return False
    except TypeError:
        return False
    if credit.interest < 0:
        return False
    if credit.type == 'diff':
        try:
            credit.principal = float(credit.principal)
        except ValueError:
            return False
        if credit.principal <= 0:
            return False
        try:
            credit.periods = int(credit.periods)
        except ValueError:
            return False
        if credit.periods < 0:
            return False
        return True
    elif credit.type == 'annuity':
        if (bool(credit.periods) + bool(credit.payment) + bool(credit.principal)) < 2:
            return False
        if credit.payment:
            try:
                credit.payment = float(credit.payment)
            except ValueError:
                return False
            if credit.payment < 0:
                return False
        if credit.principal:
            try:
                credit.principal = float(credit.principal)
            except ValueError:
                return False
            if credit.principal < 0:
                return False
        if credit.periods:
            try:
                credit.periods = int(credit.periods)
            except ValueError:
                return False
            if credit.periods < 0:
                return False
        return True
    else:
        return False


def annuity_credit(credit):
    if not credit.periods:
        nominal_interest_rate = credit.interest / (12 * 100)
        credit.periods = math.ceil(math.log((credit.payment / (credit.payment - nominal_interest_rate * credit.principal)), 1 + nominal_interest_rate))
        if (payment_years := credit.periods // 12) != 0:
            print(f'You need {payment_years} years', end='')
            if (payment_months := credit.periods % 12) != 0:
                print(f' and {payment_months} months', end='')
        elif (payment_months := credit.periods % 12) != 0:
            print(f'You need {payment_months} months', end='')
        print(' to repay this credit!')
    elif not credit.payment:
        nominal_interest_rate = credit.interest / (12 * 100)
        annuity_coefficient = nominal_interest_rate * ((1 + nominal_interest_rate) ** credit.periods) / \
                              ((1 + nominal_interest_rate) ** credit.periods - 1)
        credit.payment = math.ceil(credit.principal * annuity_coefficient)
        print(f'Your annuity payment = {credit.payment}!')
    elif not credit.principal:
        nominal_interest_rate = credit.interest / (12 * 100)
        annuity_coefficient = nominal_interest_rate * ((1 + nominal_interest_rate) ** credit.periods) / \
                              ((1 + nominal_interest_rate) ** credit.periods - 1)
        credit.principal = math.floor(credit.payment / annuity_coefficient)
        print(f'Your credit principal = {credit.principal}!')
    Overpayment = math.ceil(credit.payment * credit.periods - credit.principal)
    print(f'\n{Overpayment = }')


def diff_credit(credit):
    total_paid = 0
    nominal_interest_rate = credit.interest / (12 * 100)
    for month in range(credit.periods):
        payment = math.ceil((credit.principal / credit.periods) + nominal_interest_rate * (credit.principal - (credit.principal * month / credit.periods)))
        total_paid += payment
        print(f'Month {month + 1}: paid out {payment}')
    Overpayment = math.ceil(total_paid - credit.principal)
    print(f'\n{Overpayment = }')


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-t", "--type", required=False,
                        help='Indicates the type of payments: "annuity" or "diff" (differentiated).')
arg_parser.add_argument("-p", "--payment", required=False, help='Monthly payment')
arg_parser.add_argument("-c", "--principal", required=False, help='Credit principal')
arg_parser.add_argument("-d", "--periods", required=False, help='Number of months and/or years needed to repay the '
                                                                'credit')
arg_parser.add_argument("-i", "--interest", required=False, help='Interest specified without a percent sign')
args = arg_parser.parse_args()

if arguments_correct(args):
    if args.type == 'diff':
        diff_credit(args)
    else:
        annuity_credit(args)
else:
    print('Incorrect parameters.')



