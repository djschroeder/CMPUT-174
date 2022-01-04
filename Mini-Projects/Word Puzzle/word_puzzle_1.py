# Word Puzzle Game

import random

# display instructions
filename = 'wp_instructions.txt'
filemode = 'r'
infile = open(filename,filemode)
instructions = infile.read()
infile.close()
print(instructions)

# choose word randomly from words list
word_list = ['apple','banana','watermelon','kiwi','pineapple','mango']
random_word = random.choice(word_list)
character_list = list(random_word)
unknown_word = []
for character in character_list:
    unknown_word.append('_')
    
# print remaining characters in the word
print('The answer so far is ' + ''.join(unknown_word))
#   - prompt user to guess a letter and display remaining guesses
player_guess = input('Guess a letter: ')
index = -1
for letter in character_list:
    index = index + 1
    if player_guess == letter:
        unknown_word[index] = letter
print(''.join(unknown_word))
# if player guesses the correct word display contratulations message
#   - if player does not correctly guess after 4 guess display condolensce