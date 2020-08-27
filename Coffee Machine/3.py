water_count = int(input("Write how many ml of water the coffee machine has: "))
milk_count = int(input("Write how many ml of milk the coffee machine has: "))
coffee_beans_count = int(
    input("Write how many grams of coffee beans the coffee machine has: "))
number_of_drinks = int(input("Write how many cups of coffee you will need: "))
WATER = 200
MILK = 50
COFFEE_BEANS = 15
possible_cups = int(min(water_count / WATER, milk_count /
                        MILK, coffee_beans_count / COFFEE_BEANS))
if number_of_drinks > possible_cups:
    print(f"No, I can make only {possible_cups} cups of coffee")
elif number_of_drinks == possible_cups:
    print("Yes, I can make that amount of coffee")
else:
    print(f"Yes, I can make that amount of coffee (and even {possible_cups-number_of_drinks} more than that)")
