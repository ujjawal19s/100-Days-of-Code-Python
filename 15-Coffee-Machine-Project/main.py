MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def process_coins(quart, dim, nick, penn):
    total = 0.25 * quart + 0.10 * dim + 0.05 * nick + 0.01 * penn
    return total


def resources_sufficient(choice):
    if resources["water"] < MENU[choice]["ingredients"]["water"]:
        print("Sorry there is not enough water")
    if resources["milk"] < MENU[choice]["ingredients"]["milk"]:
        print("Sorry there is not enough milk")
    if resources["coffee"] < MENU[choice]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee")


def transaction():
    if MENU[user_choice]["cost"] > process_coins(quarters, dimes, nickles, pennies):
        print("Sorry that's not enough money. Money refunded.")
    elif resources["water"] < MENU[user_choice]["ingredients"]["water"] or resources["milk"] < MENU[user_choice]["ingredients"]["milk"] or resources["coffee"] < MENU[user_choice]["ingredients"]["coffee"]:
        resources_sufficient(user_choice)
    else:
        resources["water"] -= MENU[user_choice]["ingredients"]["water"]
        resources["milk"] -= MENU[user_choice]["ingredients"]["milk"]
        resources["coffee"] -= MENU[user_choice]["ingredients"]["coffee"]
        resources["money"] += MENU[user_choice]["cost"]

        change = process_coins(quarters, dimes, nickles, pennies) - MENU[user_choice]["cost"]
        change = round(change, 2)
        print(f"Here is ${change} in change")
        print(f"Here is your {user_choice}. Enjoy!")


should_continue = True

while should_continue:

    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    elif user_choice == "off":
        should_continue = False
    else:
        print("Please insert coins.")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickles = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))

        transaction()
