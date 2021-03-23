print ("""
Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!
""")

cup = int(input("Write how many cups of coffee you will need:\n> "))
print("For ", cup, " cups of coffee you will need:")
print(cup * 200, " ml of water")
print(cup * 50, " ml of milk")
print(cup * 15, " g of coffee beans")