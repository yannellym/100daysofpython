from art import logo, vs, lost
from game_data import data 
import random
import replit 

game_over = False
cand_a_info = ["A"]
cand_b_info = ["B"]
higher_cand = None
high_score = 0
next_level = True

def cand_a():
  global cand_a_info
  random_number = random.randint(0,49)
  cand_a_name = data[random_number]['name']
  cand_a_des = data[random_number]['description']
  cand_a_country = data[random_number]['country']
  cand_a_count = data[random_number]['follower_count']
  cand_a_info.extend([cand_a_count])
  
  print(f"Compare A: {cand_a_name}, a {cand_a_des}, from {cand_a_country}. {cand_a_count}")
 

def cand_b():
  global cand_b_info
  random_number = random.randint(0,49)
  cand_b_name = data[random_number]['name']
  cand_b_des = data[random_number]['description']
  cand_b_country = data[random_number]['country']
  cand_b_count = data[random_number]['follower_count']
  cand_b_info.extend([cand_b_count])
  
  print(f"Against B: {cand_b_name}, a {cand_b_des}, from {cand_b_country}.{cand_b_count}")

def which_is_greater(cand_a_info, cand_b_info):
  global higher_cand
  if cand_a_info.pop() > cand_b_info.pop():
    higher_cand = cand_a_info
  else:
    higher_cand = cand_b_info

def is_user_correct():
  global high_score
  user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()

  if user_answer == higher_cand[0]:
    high_score += 1
    replit.clear()
    print(f"✨✨ Correct ✨✨ Current score: {high_score}")
    to_print()
  else:
    replit.clear()
    print(f"Incorrect. Sorry you lost! Final score: {high_score}")

def to_print():
  #print(logo)
  cand_a()
  # print(vs)
  cand_b()
  print(cand_a_info, cand_b_info)
  which_is_greater(cand_a_info, cand_b_info)
  is_user_correct()
 
to_print()

