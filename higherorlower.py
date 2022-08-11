# from art import logo, vs, lost
from game_data import data 
import random
import replit 

game_over = False
cand_a_info = ["A"]
cand_a_num = 0
cand_b_info = ["B"]
cand_b_num = 0
higher_cand = [0]
high_score = 0

def cand_a():
  global cand_a_info
  global cand_a_num
  cand_a_int = cand_a_num if higher_cand[0] == "A" else random.randint(0,49)
  cand_a_num = cand_a_int
  cand_a_name = data[cand_a_int]['name']
  cand_a_des = data[cand_a_int]['description']
  cand_a_country = data[cand_a_int]['country']
  cand_a_count = data[cand_a_int]['follower_count']
  cand_a_info.extend([cand_a_count])
  print(f"higher cand: {higher_cand}")
  print(f"Compare A: {cand_a_name}, a {cand_a_des}, from {cand_a_country}. {cand_a_count}")
 

def cand_b():
  global cand_b_info
  global cand_b_num
  cand_b_int = cand_b_num if higher_cand[0] == "B" else random.randint(0,49)
  cand_b_num = cand_b_int
  cand_b_name = data[cand_b_int]['name']
  cand_b_des = data[cand_b_int]['description']
  cand_b_country = data[cand_b_int]['country']
  cand_b_count = data[cand_b_int]['follower_count']
  cand_b_info.extend([cand_b_count])
  print(f"higher cand: {higher_cand}")
  print(f"Against B: {cand_b_name}, a {cand_b_des}, from {cand_b_country}.{cand_b_count}")

def which_is_greater(cand_a_info, cand_b_info):
  global higher_cand
  if cand_a_info.pop() > cand_b_info.pop():
    higher_cand = cand_a_info
  else:
    higher_cand = cand_b_info

def is_user_correct():
  global high_score
  global next_level
  global guessed_correctly
  
  user_answer = input("Who has more followers? Type 'A' or 'B': ").upper()

  if user_answer == higher_cand[0]:
    high_score += 1
    replit.clear()
    print(f"✨✨ Correct ✨✨ Current score: {high_score}")
    to_print()
  else:
    replit.clear()
    next_level = False
    print(f"Incorrect. Sorry you lost! Final score: {high_score}")

  

def to_print():
  #print(logo)
  #print(cand_a_info, cand_b_info)
  cand_a()
  cand_b()    
  which_is_greater(cand_a_info, cand_b_info)
  is_user_correct()
  
 
to_print()

