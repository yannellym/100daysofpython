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
# Loop through the chosen word, and if the guess == the chosen word, get its indices.
# With the indices, add the guess to the display. 
# The display will show the gues in the correct position and show "_" for the unguessed letters.

display = []

for letters in chosen_word:
  display.append("_")

for i in range(len(chosen_word)):
  if chosen_word[i] == guess:
    display[i] = guess
  else:
      # print("Wrong")
print(display)
