# Detailed steps on how to build the hangman game!

import random

# Alternatively, the list of random words and ASCII art would be imported from another file as follows:
# from hangman_words import word_list
# from hangman_art import logo, stages

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#word list for game.
word_list = ["cat", "pig", "horse", "rabbit", "dog", "goat", "ant", "rat", "mouse", "duck", "goose", "turkey", "chicken", "buffalo", "bird", "sheep", "monkey", "bear", "anaconda", "lion", "tiger", "slug", "cow", "squirell", "turtle", "dolphin", "elephant", "koala", "parrot", "frog", "bee", "emu", "zebra"]


# Step 1: a random number word will be chosen from the word_list.
# The user will choose a random letter that will be stored in a variable named "guess".
# "Guess" will be compared against the chosen word and be verified to see if it is IN chosen_word.

chosen_word = random.choice(word_list)
print(chosen_word)
# Step 2: Create a variable named display that will be a list. 
# for every letter in the chosen_word add a "_" to the display.

display = []
game_over = False
lives = 6
letters_guessed = []

for letters in chosen_word:
  display.append("_")

# Step 3: Declare a variable named has_won. It will hold a value of false since the user hasn't won yet.
# declare a while loop. It will have an input where the user will guess a letter.
# Loop through the chosen word, and if the guess == the chosen word, get its indices.
# With the indices, add the guess to the display. 
# The display will show the gues in the correct position and show "_" for the unguessed letters.
# print the display
# if there are no empty spaces left, the user has won. The has_won variable is now true. 

while not game_over:
  guess = input("Guess a letter: ").lower()
  dash = "_"
      
  #Check guessed letter
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
        print(display) 
  if dash not in display:
    print(f"You win! the word was {chosen_word}")
    game_over = True
  
  if guess not in chosen_word:
    if guess not in letters_guessed:
      lives -= 1
      letters_guessed.append(guess)
      print(f"The letter is not in the word. You have {lives} lives left. Letters guessed : {letters_guessed}")
    else:
      print("You already guessed that letter")
      
    print(stages[lives])
    if lives == 0:
      print(f"You have {lives} lives left. You lose! :(")
      game_over = True
