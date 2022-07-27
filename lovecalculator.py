You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is **z**."

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_count = 0;
name2_count = 0;

name1_count += name1.count("l")
name1_count += name1.count("o")
name1_count += name1.count("v")
name1_count += name1.count("e")

name1_count += name2.count("l")
name1_count += name2.count("o")
name1_count += name2.count("v")
name1_count += name2.count("e")

name2_count += name1.count("t")
name2_count += name1.count("r")
name2_count += name1.count("u")
name2_count += name1.count("e")

name2_count += name2.count("t")
name2_count += name2.count("r")
name2_count += name2.count("u")
name2_count += name2.count("e")

love_count =  int(str(name2_count) + str(name1_count))

if love_count < 10 or love_count > 90:
    print(f"Your score is {love_count}, you go together like coke and mentos.")
elif love_count >= 40 and love_count <= 50:
    print(f"Your score is {love_count}, you are alright together.")
else:
    print(f"Your score is {love_count}.")
