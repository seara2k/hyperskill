class CoffeeMachine():

    def __init__(self):
        self.espresso = {"water": 250, "milk": 0,
                         "coffee beans": 16, "cups": 1, "money": 4}
        self.latte = {"water": 350, "milk": 75,
                      "coffee beans": 20, "cups": 1, "money": 7}
        self.cappuccino = {"water": 200, "milk": 100,
                           "coffee beans": 12, "cups": 1, "money": 6}

        self.resourse_amounts = {"water": 400, "milk": 540,
                                 "coffee beans": 120, "cups": 9, "money": 550}

    def start(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit): ")
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.print_amounts()
            elif action == "exit":
                break

    def print_amounts(self):
        print("""The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
 ${} of money
""".format(*self.resourse_amounts.values()))

    def prosessing_order(self, coffee_type):
        if len([print(f"Sorry, not enough {x}!") for x, y in self.resourse_amounts.items() if y < coffee_type[x] and x != "money"]) == 0:
            print("I have enough resources, making you a coffee!")
            self.resourse_amounts["water"] -= coffee_type["water"]
            self.resourse_amounts["milk"] -= coffee_type["milk"]
            self.resourse_amounts[
                "coffee beans"] -= coffee_type["coffee beans"]
            self.resourse_amounts["cups"] -= coffee_type["cups"]
            self.resourse_amounts["money"] += coffee_type["money"]

    def buy(self):
        coffee_choice = input(
            "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")

        if coffee_choice == "back":
            return
        elif int(coffee_choice) == 2:
            self.prosessing_order(self.latte)
        elif int(coffee_choice) == 3:
            self.prosessing_order(self.cappuccino)
        elif int(coffee_choice) == 1:
            self.prosessing_order(self.espresso)

    def fill(self):
        questions = {"water": "Write how many ml of water do you want to add: ",
                     "milk": "Write how many ml of milk do you want to add: ",
                     "coffee beans": "Write how many grams of coffee beans do you want to add: ",
                     "cups": "Write how many disposable cups of coffee do you want to add: "}
        for key, item in questions.items():
            self.resourse_amounts[key] += int(input(item))

    def take(self):
        print(f'I gave you ${self.resourse_amounts["money"]}')
        self.resourse_amounts["money"] = 0


lol = CoffeeMachine()
lol.start()
