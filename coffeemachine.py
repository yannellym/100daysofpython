from data import MENU, resources

order_again = True


def clear():
    print('\n' * 5)


def use_resources(user_money, menu_item):
    for i in resources:
        if i in menu_item['ingredients']:
            resources[i] = resources[i] - menu_item['ingredients'][i]
    resources['money'] += menu_item['cost']
    print(resources)


def get_coffee(user_money, menu_item, user_input):
    global order_again
    user_change = round(user_money - menu_item['cost'], 2)
    if user_change < 0:
        print("Sorry! You don't have enough money. Please accept your refund.")
        print(f"Total refund: ${user_money}")
    else:
        use_resources(user_money, menu_item)
        print(f"${user_change} is your change.")
        print(f"Here is your {user_input} ☕️. Enjoy!")

    user_wish = input("Do you want to order another item? Type 'yes' or 'no': ").lower()
    if user_wish == "yes":
        clear()
        order_again = True
    else:
        clear()
        order_again = False
        print("Thank you for ordering, Goodbye! ")


def order_coffee():
    user_input = input("What would you like? espresso, latte, or cappuccino?: ").lower()

    if user_input == 'report':
        for i in resources:
            print(i, ":", resources[i])
    elif user_input == "off":
        print("Powering Off. Goodbye!")
    else:
        clear()
        menu_item = MENU[user_input]
        for i in menu_item['ingredients']:
            for j in resources:
                if resources[j] < menu_item['ingredients'][i]:
                    print(f"Sorry! We do not have enough {j} for your order")
                    print("Please order another item.")
                    order_coffee()
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


while order_again:
    order_coffee()

