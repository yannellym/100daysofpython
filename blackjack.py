import random 
import replit

logo = ''' .------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           

'''
print(logo)

should_continue = True
user_cards = []
computer_cards = []
user_total = 0
computer_total = 0
computer_first_card = 0

def int_generator():
  return random.choice([11,2,3,4,5,6,7,8,9,10,10,10,10])
  
def sum_cards():
  global user_total
  global computer_total
  user_total = sum(user_cards)
  computer_total = sum(computer_cards)
  return

def clear_data():
  global user_cards
  global computer_cards
  global user_total
  global computer_total
  global computer_first_card
  user_cards = []
  computer_cards = []
  user_total = 0
  computer_total = 0
  computer_first_card = 0
  return 
  
def who_won():
  replit.clear()
  while sum(computer_cards) < 21:
    computer_cards.extend([int_generator()])
  sum_cards()
  print(f"Your final hand: {user_cards}, final score: {user_total}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_total}")
  if user_total > computer_total and user_total <= 21:
    print("You win! 🥳 ")
  elif computer_total > user_total and computer_total <= 21:
    print("Computer wins! 👾")
  elif user_total == computer_total:
    print("It's a draw! 🧐")
  else:
    if user_total > computer_total:
      print ("Computer wins!! ")
    else: 
      print("You win!! ")
  clear_data()
  play_blackjack()
    
def another_one():
  user_input = input("Type 'y' to get another card, type 'n' to pass: \n").lower()
  if user_input == "y":
    replit.clear()
    new_num = int_generator()
    if sum(user_cards) == 20 and new_num == 11:
      user_cards.extend([1])
    elif sum(user_cards) > 21:
      print("You lose :(")
      another_one()
    else:
      user_cards.extend([new_num])
      computer_cards.extend([int_generator()])
    sum_cards()
    print(f"Your cards: {user_cards}, current score: {user_total}")
    if sum(user_cards) < 21:
      another_one()
    else:
      who_won()
  else:
      who_won()
  
def play_blackjack():
  global should_continue
  global computer_cards
  global computer_first_card
  
  new_game = input("Do you want to play a game of BlackJack? Type 'y' for yes or 'n' for no: \n")
  replit.clear()
  if new_game == "y":
    user_cards.extend([int_generator(),int_generator()])
    computer_first_card = int_generator()
    computer_cards += [computer_first_card]
    sum_cards()
    print(f"Your cards: {user_cards}, current score: {user_total}")
    print(f"Computer's first card: {computer_first_card}") 
    another_one() 
  else:
    replit.clear()
    print("Maybe next time! Thank you for visiting")

play_blackjack()



