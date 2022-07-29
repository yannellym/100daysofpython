import random

#word list for game.
word_list = ["cat", "pig", "horse", "rabbit", "dog", "goat", "ant", "rat", "mouse", "duck", "goose", "turkey", "chicken", "buffalo", "bird", "sheep", "monkey", "bear", "anaconda", "lion", "tiger", "slug", "cow", "squirell", "turtle", "dolphin", "elephant", "koala", "parrot", "frog", "bee", "emu", "zebra"]


# Step 1: a random number word will be chosen from the word_list.
# The user will choose a random letter that will be stored in a variable named "guess".
# "Guess" will be compared against the chosen word and be verified to see if it is IN chosen_word.

chosen_word = randon.choice(word_list)
 
guess = input("Guess a letter \n").lower()

print(guess in chosen_word)
  
# Step 2: Create a variable named display that will be a list. 
# for every letter in the chosen_word add a "_" to the display.

display = []

for letters in chosen_word:
  display.append("_")


# Step 3: Declare a variable named has_won. It will hold a value of false since the user hasn't won yet.
# declare a while loop. It will have an input where the user will guess a letter.
# Loop through the chosen word, and if the guess == the chosen word, get its indices.
# With the indices, add the guess to the display. 
# The display will show the gues in the correct position and show "_" for the unguessed letters.
# print the display
# if there are no empty spaces left, the user has won. The has_won variable is now true. 

has_won = False

while not has_won:
  guess = input("Guess a letter: ").lower()
  dash = "_"
  #Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
        print(display)
    if dash not in display:
      print(f"You win! the word was {chosen_word}")
      has_won = True
