from data import MENU, resources


def clear():
    print('\n' * 10)


def get_change(user_money, item):
    user_change = round(user_money - MENU[item]['cost'],2)
    if user_change < 0:
        print("Sorry! You don't have enough money. Please accept your refund.")
        get_my_coffee()
    else:
        print(f"Here is ${user_change} in change.")
        print(f"Here is your {item} ☕️. Enjoy!")
        return user_change


def get_my_coffee():
    user_input = input("What would you like? espresso, latte, or cappuccino?: ").lower()

    if user_input == 'report':
        for i in resources:
            print(i, ":", resources[i])
    elif user_input == "off":
        print("Powering Off. Goodbye!")
    else:
        clear()
        print("Please insert coins.")
        user_quarters = int(input("How many quarters?: ")) * .25
        user_dimes = int(input("How many dimes?: ")) * .10
        user_nickles = int(input("How many nickles?: ")) * .05
        user_pennies = int(input("How many pennies?: ")) * .01
        user_money = sum([user_pennies, user_nickles, user_dimes, user_quarters])
        clear()
        print(f"You gave me ${user_money} in total. ")

        if user_input == 'espresso':
            user_change = get_change(user_money, 'espresso')
        elif user_input == 'latte':
            user_change = get_change(user_money, 'latte')
        else:
            user_change = get_change(user_money, 'cappuccino')


get_my_coffee()
