from turtle import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the secret auction program")

bidders = {}

active_auction = True
highest_bidder = ""
highest_bid = 0

def input_bidder():
    global active_auction
    bidder_name = input("What is your name?  \n")
    bidder_bid = int(input("What is your bid ? \n $"))

    bidders[bidder_name] = bidder_bid
    additional_bidder = input("Are there any other bidders ? Type Yes or No \n").lower()
  
    if additional_bidder == "yes":
        input_bidder()
    else:
        active_auction = False

def highest_bidder():
    global highest_bidder
    global highest_bid
    for k, v in bidders.items():
        if v> highest_bid:
            highest_bidder = k
            highest_bid = v
    clear()
    print(f"The highest bidder is {highest_bidder} with a bid of $ {highest_bid}.")

while active_auction:
    input_bidder()
    highest_bidder()


