from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True


def clear():
    print("\n" * 10)


while is_on:
    options = menu.get_items()
    chosen_drink = input(f"Which drink would you like? ({options}) ")
    clear()
    if chosen_drink == "report":
        coffee_maker.report()
        money_machine.report()
    elif chosen_drink == "off":
        print("Powering off. Goodbye!")
        is_on = False
    else:
        drink_from_menu = menu.find_drink(chosen_drink)
        if coffee_maker.is_resource_sufficient(drink_from_menu) and money_machine.make_payment(drink_from_menu.cost):
            coffee_maker.make_coffee(drink_from_menu)

