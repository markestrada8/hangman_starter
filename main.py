# Import needed libraries
from data import words
import random

# Create a python list from the words in the data file for the project (don't worry about this right now)
words_list = [word for word in words.split('\n')[1:-1]]

# Uncomment to print out the words list (there are a little over 200)
# print(words_list)

# DIFFICULT: Choose a random word from the list of words
# word = random.choice(words_list)

# TO START: Choose a predetermined word from the list of words
word = words_list[5]

# TODO: Welcome the player


# TODO: Establish a means of keeping score (8 guesses is a pretty good number of 'lives')


# TODO: Somehow display 'blanks' (try underscores: "______") to represent the number of characters in their word (maybe a loop?)


# TODO: Have the player guess a letter with an input, and check if that letter is in the word


# TODO: Replace (ALL) the corresponding blanks with that letter if they choose correctly and display the new partial word ("__s__s") to the player
# Remember: you can mutate (alter) a list, but not a string, so you might have to convert it back and forth


# TODO: Subtract a guess if they choose wrong and use print to tell the player


# TODO: Now the difficult part - run the process again, and have the player choose another letter! (A for loop can work, but try to use a while loop - remember to set an exit condition)


# TODO: If the player runs out of guesses they lose. If the blanks are all filled, they win! Close your loop and end the program or maybe try to let the player choose to play again...

print('Hello, world')
