espresso = {"water": 250, "milk": 0, "coffee beans": 16, "cups": 1, "money": 4}
latte = {"water": 350, "milk": 75, "coffee beans": 20, "cups": 1, "money": 7}
cappuccino = {"water": 200, "milk": 100,
              "coffee beans": 12, "cups": 1, "money": 6}

resourse_amounts = {"water": 400, "milk": 540,
                    "coffee beans": 120, "cups": 9, "money": 550}


def prosessing_order(coffee_type):
    if len([print(f"Sorry, not enough {x}!") for x, y in resourse_amounts.items() if y < coffee_type[x] and x != "money"]) == 0:
        print("I have enough resources, making you a coffee!")
        resourse_amounts["water"] -= coffee_type["water"]
        resourse_amounts["milk"] -= coffee_type["milk"]
        resourse_amounts["coffee beans"] -= coffee_type["coffee beans"]
        resourse_amounts["cups"] -= coffee_type["cups"]
        resourse_amounts["money"] += coffee_type["money"]


def buy():
    coffee_choice = input(
        "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")

    if coffee_choice == "back":
        return
    elif int(coffee_choice) == 2:
        prosessing_order(latte)
    elif int(coffee_choice) == 3:
        prosessing_order(cappuccino)
    elif int(coffee_choice) == 1:
        prosessing_order(espresso)


def fill():
    questions = {"water": "Write how many ml of water do you want to add: ",
                 "milk": "Write how many ml of milk do you want to add: ",
                 "coffee beans": "Write how many grams of coffee beans do you want to add: ",
                 "cups": "Write how many disposable cups of coffee do you want to add: "}
    for key, item in questions.items():
        resourse_amounts[key] += int(input(item))


def take():
    print(f'I gave you ${resourse_amounts["money"]}')
    resourse_amounts["money"] = 0


def print_amounts():
    print("""The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
${} of money
    """.format(*resourse_amounts.values()))

while True:
    action = input("Write action (buy, fill, take, remaining, exit): ")
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        print_amounts()
    elif action == "exit":
        break
