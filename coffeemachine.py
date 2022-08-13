from data import MENU, resources


def clear():
    print('\n' * 10)


def get_coffee(user_money, menu_item, user_input):
    user_change = round(user_money - menu_item['cost'], 2)
    if user_change < 0:
        print("Sorry! You don't have enough money. Please accept your refund.")
        order_coffee()
    else:
        print(f"${user_change} is your change.")
        print(f"Here is your {user_input} ☕️. Enjoy!")
        return


def order_coffee():
    user_input = input("What would you like? espresso, latte, or cappuccino?: ").lower()
    menu_item = MENU[user_input]
    if user_input == 'report':
        for i in resources:
            print(i, ":", resources[i])
    elif user_input == "off":
        print("Powering Off. Goodbye!")
    else:
        clear()
        for i in menu_item['ingredients']:
            for j in resources:
                if resources[j] < menu_item['ingredients'][i]:
                    print("not enough")
                else:
                    clear()
                    print(f"The {user_input} costs ${menu_item['cost']} ")
                    print("Please insert coins.")
                    user_quarters = int(input("How many quarters?: ")) * .25
                    user_dimes = int(input("How many dimes?: ")) * .10
                    user_nickles = int(input("How many nickles?: ")) * .05
                    user_pennies = int(input("How many pennies?: ")) * .01
                    user_money = sum([user_pennies, user_nickles, user_dimes, user_quarters])

                    clear()
                    print(f"You gave me ${user_money} in total. ")
                    return get_coffee(user_money, menu_item, user_input)


order_coffee()

