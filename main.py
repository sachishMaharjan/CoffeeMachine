from data import MENU, resources


# TODO 4: Check resources sufficient?
def check_resources(water, milk, coffee, drinks):
    """
    Takes current water, milk, coffee level and returns remaining water, milk, coffee level.
    """
    current_drink_ingredients = MENU[drinks]["ingredients"]
    if drinks == "espresso":
        if water >= current_drink_ingredients["water"] and coffee >= current_drink_ingredients["coffee"]:
            water -= current_drink_ingredients["water"]
            coffee -= current_drink_ingredients["coffee"]
            return True, water, milk, coffee
        else:
            print("Sorry there are not enough resources")
            return False, water, milk, coffee
    else:
        if water >= current_drink_ingredients["water"] and milk >= current_drink_ingredients["milk"] and coffee >= \
                current_drink_ingredients["coffee"]:
            water -= current_drink_ingredients["water"]
            milk -= current_drink_ingredients["milk"]
            coffee -= current_drink_ingredients["coffee"]
            return True, water, milk, coffee
        else:
            print("Sorry there are not enough resources")
            return False, water, milk, coffee


# TODO 5:  Process coins.

def process_coins(quarters, dimes, nickles, pennies, current_drink):
    """
    Takes total coins inserted and current drink and returns True if enough funds and remaining change.

    """
    inserted_coins = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    cost_of_drink = MENU[current_drink]["cost"]

    if inserted_coins > cost_of_drink:
        change = round((inserted_coins - cost_of_drink), 2)
        print(f"Here is ${change} in change.")
        # TODO 7: Make Coffee.
        print(f"Here is your {current_drink} ☕️. Enjoy!")
        return True, cost_of_drink
    else:
        print(f"Sorry that's not enough money. Money refunded")
        return False, 0


# TODO 3: Print report.
current_water = resources["water"]
current_milk = resources["milk"]
current_coffee = resources["coffee"]
current_money = 0
machine_on = True

while machine_on:
    # TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    drink_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO 2: Turn off the Coffee Machine by entering "off" to the prompt.
    if drink_choice == "off":
        machine_on = False

    elif drink_choice == "report":
        print(f"Water: {current_water}")
        print(f"Milk: {current_milk}")
        print(f"Coffee: {current_coffee}")
        print(f"Money: {current_money}")

    else:
        enough_resources, deducted_water, deducted_milk, deducted_coffee = check_resources(current_water, current_milk, current_coffee, drink_choice)
        if enough_resources:
            print("Please insert coins.")
            inserted_quarters = int(input("how many quarters?: "))
            inserted_dimes = int(input("how many dimes?: "))
            inserted_nickles = int(input("how many nickles?: "))
            inserted_pennies = int(input("how many pennies?: "))

            # TODO 6: Check transaction successful?
            enough_money, drink_cost = process_coins(inserted_quarters, inserted_dimes, inserted_nickles, inserted_pennies, drink_choice)
            current_money += drink_cost
            if enough_money:
                current_water = deducted_water
                current_milk = deducted_milk
                current_coffee = deducted_coffee


