import random 
import replit

logo = ''' 
 ██████╗ ██╗   ██╗███████╗███████╗███████╗    ████████╗██╗  ██╗ █████╗ ████████╗
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝    ╚══██╔══╝██║  ██║██╔══██╗╚══██╔══╝
██║  ███╗██║   ██║█████╗  ███████╗███████╗       ██║   ███████║███████║   ██║   
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║       ██║   ██╔══██║██╔══██║   ██║   
╚██████╔╝╚██████╔╝███████╗███████║███████║       ██║   ██║  ██║██║  ██║   ██║   
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
          ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ ██╗                       
          ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗██║                       
          ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝██║                       
          ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗╚═╝                       
          ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║██╗                       
          ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝
  '''
congrats = '''
 ██████╗ ██████╗ ███╗   ██╗ ██████╗ ██████╗  █████╗ ████████╗███████╗    ██╗
██╔════╝██╔═══██╗████╗  ██║██╔════╝ ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝    ██║
██║     ██║   ██║██╔██╗ ██║██║  ███╗██████╔╝███████║   ██║   ███████╗    ██║
██║     ██║   ██║██║╚██╗██║██║   ██║██╔══██╗██╔══██║   ██║   ╚════██║    ╚═╝
╚██████╗╚██████╔╝██║ ╚████║╚██████╔╝██║  ██║██║  ██║   ██║   ███████║    ██╗
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚═╝
'''
game_over = ''' 
  ▄████ ▄▄▄      ███▄ ▄███▓█████     ▒█████  ██▒   █▓█████ ██▀███  
 ██▒ ▀█▒████▄   ▓██▒▀█▀ ██▓█   ▀    ▒██▒  ██▓██░   █▓█   ▀▓██ ▒ ██▒
▒██░▄▄▄▒██  ▀█▄ ▓██    ▓██▒███      ▒██░  ██▒▓██  █▒▒███  ▓██ ░▄█ ▒
░▓█  ██░██▄▄▄▄██▒██    ▒██▒▓█  ▄    ▒██   ██░ ▒██ █░▒▓█  ▄▒██▀▀█▄  
░▒▓███▀▒▓█   ▓██▒██▒   ░██░▒████▒   ░ ████▓▒░  ▒▀█░ ░▒████░██▓ ▒██▒
 ░▒   ▒ ▒▒   ▓▒█░ ▒░   ░  ░░ ▒░ ░   ░ ▒░▒░▒░   ░ ▐░ ░░ ▒░ ░ ▒▓ ░▒▓░
  ░   ░  ▒   ▒▒ ░  ░      ░░ ░  ░     ░ ▒ ▒░   ░ ░░  ░ ░  ░ ░▒ ░ ▒░
░ ░   ░  ░   ▒  ░      ░     ░      ░ ░ ░ ▒      ░░    ░    ░░   ░ 
      ░      ░  ░      ░     ░  ░       ░ ░       ░    ░  ░  ░     
                                                 ░          '''

def welcome_user():
  print(logo)
  print("Welcome to the 'Guess That Number!' game")
  print("I'm thinking of a number between 1 and 100.")
  return input("Choose a difficulty. Type 'easy' or 'hard' : \n").lower()
  
def user_input():
  user_guess = int(input("Guess the number: "))
  return user_guess


def guess_number():
  user_won = False
  attempts_left = 0
  difficulty_level =  welcome_user()
  correct_number = random.randint(1,100)

  replit.clear()
  
  if difficulty_level == "easy":
    attempts_left = 10
  else: 
    attempts_left = 5
    
  #print(f"shh! the correct number is {correct_number}") 
  print(f"You have {attempts_left} attempts left") 
  number_guessed = user_input()
  
  while not user_won:
    if attempts_left == 1:
      user_won = True
      replit.clear()
      print(game_over)
      print("Game Over ☹️ Sorry you lost! ")
      continue_game = input("Play again? Type 'y' for yes or 'n' for no: ")
      
      if continue_game == 'y':
        user_won = False
        attempts_left = 0
        difficulty_level =  ""
        correct_number = 0
        replit.clear()
        guess_number()
      else:
          print("Goodbye. Thank you for playing! 🙂")
    else:
      replit.clear()
      attempts_left -= 1      
      
      if number_guessed < correct_number:
        print(f"Too low :( Guess again. The num is {correct_number}")
      elif number_guessed == correct_number:
        user_won = True
        print(congrats)
        print(f"The correct number was {correct_number}. You won! 🥳 ")
        continue_game = input("Play again? Type 'y' for yes or 'n' for no: ")
        
        if continue_game == 'y':
          user_won = False
          attempts_left = 0
          difficulty_level =  ""
          correct_number = 0
          replit.clear()
          guess_number()
        else:
          print("Goodbye. Thank you for playing! 🙂")
      else:
        print(f"Too high! guess again. The num is {correct_number}")
      print(f"You have {attempts_left} attempts left") 
        
      number_guessed = user_input()



  

guess_number()
