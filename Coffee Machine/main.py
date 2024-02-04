from menu import MENU, resources


def required_resources(chosen_drink):
    """resources needed for each drink"""
    espresso = MENU["espresso"]["ingredients"]
    latte = MENU["latte"]["ingredients"]
    cappuccino = MENU["cappuccino"]["ingredients"]

    water_used = 0
    milk_used = 0
    coffee_used = 0

    if chosen_drink == "espresso":

        espresso_water = espresso["water"]
        espresso_coffee = espresso["coffee"]
        water_used += espresso_water
        coffee_used += espresso_coffee

        return water_used, milk_used, coffee_used

    elif chosen_drink == "latte":

        latte_water = latte["water"]
        latte_milk = latte["milk"]
        latte_coffee = latte["coffee"]
        water_used += latte_water
        milk_used += latte_milk
        coffee_used += latte_coffee

        return water_used, milk_used, coffee_used

    elif chosen_drink == "cappuccino":

        cappuccino_water = cappuccino["water"]
        cappuccino_milk = cappuccino["milk"]
        cappuccino_coffee = cappuccino["coffee"]
        water_used += cappuccino_water
        milk_used += cappuccino_milk
        coffee_used += cappuccino_coffee

        return water_used, milk_used, coffee_used

    else:
        return water_used, milk_used, coffee_used


def report(water, coffee, milk):
    """Check the resources available"""

    print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}")


def change(chosen_drink):
    """Give the client's change | Refund coins if inserted less than needed"""
    print("Please insert coins.")

    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    chosen_drink_cost = MENU[chosen_drink]["cost"]
    total_coins_inserted = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    client_change = round(total_coins_inserted - chosen_drink_cost, 2)

    if total_coins_inserted < chosen_drink_cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print(f"Here is ${client_change} in change.")
        print(f"Here is your {chosen_drink}. Enjoy!")


initial_water = resources["water"]
initial_milk = resources["milk"]
initial_coffee = resources["coffee"]

water_count = 0
milk_count = 0
coffee_count = 0
is_on = True

while is_on:

    user_choice = input("   What would you like? (espresso/latte/cappuccino): ").lower()
    water_needed, milk_needed, coffee_needed = required_resources(chosen_drink=user_choice)

    water_count += water_needed
    coffee_count += coffee_needed
    milk_count += milk_needed

    available_water = initial_water - water_count
    available_coffee = initial_coffee - coffee_count
    available_milk = initial_milk - milk_count

    if user_choice == "report":
        report(water=available_water, coffee=available_coffee, milk=available_milk)
    elif user_choice == "off":
        is_on = False
    else:
        if available_water < 0:
            print(" Sorry, there is not enough water.")
        elif available_coffee < 0:
            print(" Sorry, there is not enough coffee.")
        elif available_milk < 0:
            print(" Sorry, there is not enough milk.")
        else:
            change(chosen_drink=user_choice)

