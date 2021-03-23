WATER = 400
MILK = 540
COFFEE_BEAN = 120
CUPS = 9
MONEY = 550

def display():
    print("The coffee machine has:")
    print(WATER, "of water")
    print(MILK, "of milk")
    print(COFFEE_BEAN, "of coffee beans")
    print(CUPS, "of disposable cups")
    print(MONEY, "of money")

def buy_function():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n> ", end = '')
    action = int(input())

    global WATER
    global MILK
    global MONEY
    global COFFEE_BEAN
    global CUPS

    if action == 1:
        WATER = WATER - 250
        COFFEE_BEAN = COFFEE_BEAN - 16
        MONEY = MONEY + 4
        CUPS = CUPS - 1
    elif action == 2:
        WATER = WATER - 350
        MILK = MILK - 75
        COFFEE_BEAN = COFFEE_BEAN - 20
        MONEY = MONEY + 7
        CUPS = CUPS - 1
    elif action == 3:
        WATER = WATER - 200
        MILK = MILK - 100
        COFFEE_BEAN = COFFEE_BEAN - 12
        MONEY = MONEY + 6
        CUPS = CUPS - 1
    print()
    display()


def fill_function():
    global WATER
    global MILK
    global MONEY
    global COFFEE_BEAN
    global CUPS

    print("Write how many ml of water do you want to add:\n> ", end = '')
    WATER = WATER + int(input())
    print("Write how many ml of milk do you want to add:\n> ", end = '')
    MILK = MILK + int(input())
    print("Write how many grams of coffee beans do you want to add:\n> ", end = '')
    COFFEE_BEAN = COFFEE_BEAN + int(input())
    print("Write how many disposable cups of coffee do you want to add:\n> ", end = '')
    CUPS = CUPS + int(input())

    print()
    display()


def take_function():
    global MONEY

    print("I gave you $", end = '')
    print(MONEY)
    MONEY = 0
    print()
    display()



def write_action():
    print("Write action (buy, fill, take):\n> ", end = '')
    action = input()

    if action == 'buy':
        buy_function()
    elif action == 'fill':
        fill_function()
    elif action == 'take':
        take_function()

display()
write_action()