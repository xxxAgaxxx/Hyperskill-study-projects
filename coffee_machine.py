print('Starting to make a coffee', 'Grinding coffee beans', 'Boiling water',
      'Mixing boiled water with crushed coffee beans',
      'Pouring coffee into the cup', 'Pouring some milk into the cup',
      'Coffee is ready!', sep='\n')

current_supplies = {'water': int(400), 'milk': int(540), 'beans': int(120), 'cups': int(9), 'cash': int(550)}
action = ''
espresso_drain = {'water': int(-250), 'milk': int(0), 'beans': int(-16), 'cups': int(-1), 'cash': int(4)}
latte_drain = {'water': int(-350), 'milk': int(-75), 'beans': int(-20), 'cups': int(-1), 'cash': int(7)}
cappuccino_drain = {'water': int(-200), 'milk': int(-100), 'beans': int(-12), 'cups': int(-1), 'cash': int(6)}


def machine_state():
    global current_supplies
    print(
        'The machine has:\n{water} of water\n{milk} of milk\n{beans} of coffee beans'
        '\n{cups} of disposable cups\n${cash} of money'.format(**current_supplies))


def get_action():
    global action
    action = input("U wanna buy, fill, take money, get remaining supplies, or exit? ")
    return 0


def check_supplies(coffee_variety):
    if (coffee_variety == '1') or (coffee_variety == 'espresso'):
        for key in current_supplies:
            if key in espresso_drain and key != 'cash':
                if current_supplies[key] + espresso_drain[key] < 0:
                    print('Sorry, not enough {}!'.format(key))
                    return 1
            else:
                pass
    if (coffee_variety == '2') or (coffee_variety == 'latte'):
        for key in current_supplies:
            if key in latte_drain and key != 'cash':
                if current_supplies[key] + latte_drain[key] <= 0:
                    print('Sorry, not enough {}!'.format(key))
                    return 1
            else:
                pass
    if (coffee_variety == '3') or (coffee_variety == 'cappuccino'):
        for key in current_supplies:
            if key in cappuccino_drain and key != 'cash':
                if current_supplies[key] + cappuccino_drain[key] <= 0:
                    print('Sorry, not enough {}!'.format(key))
                    return 1
            else:
                pass
    return 0


def sell_coffee():
    global current_supplies
    coffee_variety = input('Which coffee you want? 1 — espresso, 2 — latte, 3 — cappuccino, back — to main menu: ')
    if check_supplies(coffee_variety):
        return 2
    if (coffee_variety == '1') or (coffee_variety == 'espresso'):
        for key in current_supplies:
            if key in espresso_drain:
                current_supplies[key] += espresso_drain[key]
            else:
                pass
        return 0
    if (coffee_variety == '2') or (coffee_variety == 'latte'):
        for key in current_supplies:
            if key in latte_drain:
                current_supplies[key] += latte_drain[key]
            else:
                pass
        return 0
    if (coffee_variety == '3') or (coffee_variety == 'cappuccino'):
        for key in current_supplies:
            if key in cappuccino_drain:
                current_supplies[key] += cappuccino_drain[key]
            else:
                pass
        return 0
    if coffee_variety == 'back':
        return 0
    return 1


def renew_machine():
    global current_supplies
    current_supplies['water'] += int(input('Write how many ml of water do you want to add: '))
    current_supplies['milk'] += int(input('Write how many ml of milk do you want to add: '))
    current_supplies['beans'] += int(input('Write how many grams of coffee beans do you want to add: '))
    current_supplies['cups'] += int(input('Write how many disposable cups of coffee do you want to add: '))
    return 0


def collector():
    global current_supplies
    if current_supplies['cash'] == 0:
        print('I have no cash, come back later!')
    else:
        print('I gave you ', current_supplies['cash'])
        current_supplies['cash'] = 0
    return 0


while True:
    get_action()
    if action == 'buy':
        troll_counter = 0
        while sell_coffee() == True:
            if sell_coffee() == 0:
                if troll_counter < 5:
                    print("Please choose correct coffee variety!")
                    troll_counter += 1
                    continue
                else:
                    break
            if sell_coffee() == 2:
                break

    if action == 'fill':
        renew_machine()
    if action == 'take':
        collector()
    if action == 'exit':
        break
    if action == 'remaining':
        machine_state()
    else:
        continue
