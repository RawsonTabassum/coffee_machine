import math

WATER = 200
MILK = 50
COFFEE = 15

water_in_machine = int(input("Write how many ml of water the coffee machine has:\n> "))
milk_in_machine = int(input("Write how many ml of milk the coffee machine has:\n> "))
coffee_in_machine = int(input("Write how many grams of coffee beans the coffee machine has:\n> "))

coffee_needed = int(input("Write how many cups of coffee you will need:\n> "))

possible_amount = min(math.floor(water_in_machine / WATER),
                  min((math.floor(milk_in_machine / MILK)), math.floor(coffee_in_machine / COFFEE)))

if possible_amount == coffee_needed:
    print('Yes, I can make that amount of coffee')
elif possible_amount < coffee_needed:
    print('No, I can make only ', possible_amount, ' cups of coffee')
else:
    print('Yes, I can make that amount of coffee (and even ',
          possible_amount - coffee_needed, ' more than that)')