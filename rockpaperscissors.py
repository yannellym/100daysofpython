rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choices = { 0: rock, 1: paper, 2: scissors}

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
computer_choice = random.randint(0,2)

# print(choices[user_choice])
# print(choices[computer_choice])

if user_choice == 0 and computer_choice == 2:
  print(f"You chose {choices[user_choice]}, computer chose {choices[computer_choice]}. You Win!")
elif user_choice == 0 and computer_choice == 1:
  print(f"You chose {choices[user_choice]}, computer chose {choices[computer_choice]}. You Lose!")
elif user_choice ==  1 and computer_choice == 0:
  print(f"You chose {choices[user_choice]}, computer chose {choices[computer_choice]}. You Win!")
elif user_choice == 1 and computer_choice == 2:
  print(f"You chose {choices[user_choice]}, computer chose {choices[computer_choice]}. You Lose!")
elif user_choice ==  2 and computer_choice == 0:
  print(f"You chose {choices[user_choice]}, computer chose {choices[computer_choice]}. You Lose!")
elif user_choice == 2 and computer_choice == 1:
  print(f"You chose {choices[user_choice]}, computer chose {choices[computer_choice]}. You Win!")
else:
  print(f"You chose {choices[user_choice]}, computer chose {choices[computer_choice]}. It's a tie!")
