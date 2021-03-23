WATER = 400
MILK = 540
COFFEE_BEAN = 120
CUPS = 9
MONEY = 550

def check_for_espresso():
    global WATER
    global MILK
    global MONEY
    global COFFEE_BEAN
    global CUPS

    if WATER >= 250 and COFFEE_BEAN >= 16 and CUPS >= 1:
        print("I have enough resources, making you a coffee!\n")

        WATER = WATER - 250
        COFFEE_BEAN = COFFEE_BEAN - 16
        MONEY = MONEY + 4
        CUPS = CUPS - 1
    elif WATER < 250:
        print("Sorry, not enough water!\n")
    elif COFFEE_BEAN < 16:
        print("Sorry, not enough coffee bean!\n")
    elif CUPS < 1:
        print("Sorry, not enough cups!\n")


def check_for_latte():
    global WATER
    global MILK
    global MONEY
    global COFFEE_BEAN
    global CUPS

    if WATER >= 350 and MILK >= 75 and COFFEE_BEAN >= 20 and CUPS >= 1:
        print("I have enough resources, making you a coffee!\n")

        WATER = WATER - 350
        MILK = MILK - 75
        COFFEE_BEAN = COFFEE_BEAN - 20
        MONEY = MONEY + 7
        CUPS = CUPS - 1
    elif WATER < 350:
        print("Sorry, not enough water!\n")
    elif MILK < 75:
        print("Sorry, not enough milk!\n")
    elif COFFEE_BEAN < 20:
        print("Sorry, not coffee bean!\n")
    elif CUPS < 1:
        print("Sorry, not enough cups!\n")


def check_for_cappuccino():
    global WATER
    global MILK
    global MONEY
    global COFFEE_BEAN
    global CUPS

    if WATER >= 200 and MILK >= 100 and COFFEE_BEAN >= 12 and CUPS >= 1:
        print("I have enough resources, making you a coffee!\n")

        WATER = WATER - 200
        MILK = MILK - 100
        COFFEE_BEAN = COFFEE_BEAN - 12
        MONEY = MONEY + 6
        CUPS = CUPS - 1

    elif WATER < 200:
        print("Sorry, not enough water!\n")
    elif MILK < 100:
        print("Sorry, not enough milk!\n")
    elif COFFEE_BEAN < 12:
        print("Sorry, not coffee bean!\n")
    elif CUPS < 1:
        print("Sorry, not enough cups!\n")




def buy_function():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n> ", end='')
    action = input()

    global WATER
    global MILK
    global MONEY
    global COFFEE_BEAN
    global CUPS

    if action == '1':
        check_for_espresso()
    elif action == '2':
        check_for_latte()
    elif action == '3':
        check_for_cappuccino()
    elif action == 'back':
        print()

    write_action()



def fill_function():
    global WATER
    global MILK
    global MONEY
    global COFFEE_BEAN
    global CUPS

    print("Write how many ml of water do you want to add:\n> ", end='')
    WATER = WATER + int(input())
    print("Write how many ml of milk do you want to add:\n> ", end='')
    MILK = MILK + int(input())
    print("Write how many grams of coffee beans do you want to add:\n> ", end='')
    COFFEE_BEAN = COFFEE_BEAN + int(input())
    print("Write how many disposable cups of coffee do you want to add:\n> ", end='')
    CUPS = CUPS + int(input())
    print()

    write_action()




def take_function():
    global MONEY

    print("I gave you $", end='')
    print(MONEY)
    MONEY = 0
    print()

    write_action()



def remaining_function():
    global WATER
    global MILK
    global MONEY
    global COFFEE_BEAN
    global CUPS

    print("The coffee machine has:")
    print(WATER, "of water")
    print(MILK, "of milk")
    print(COFFEE_BEAN, "of coffee beans")
    print(CUPS, "of disposable cups")
    if MONEY > 0:
        print("$", end = '')
        print(MONEY, "of money")
    else:
        print(MONEY, "of money")
    print()

    write_action()




def write_action():
    flag = True
    print("Write action (buy, fill, take, remaining, exit):\n> ", end = '')
    action = input()

    if action == 'buy':
        print()
        buy_function()
    elif action == 'fill':
        print()
        fill_function()
    elif action == 'take':
        print()
        take_function()
    elif action == 'remaining':
        print()
        remaining_function()
    elif action == 'exit':
        return



write_action()