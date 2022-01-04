# Word Puzzle Game

import random

# display instructions
filename = 'wp_instructions.txt'
filemode = 'r'
infile = open(filename,filemode)
instructions = infile.read()
infile.close()
print(instructions)

# variables
guessed_letters = set()
tries = 4

# choose word randomly from words list
word_list = ['apple','banana','watermelon','kiwi','pineapple','mango']
random_word = random.choice(word_list)
character_list = list(random_word)
unknown_word = []
for character in character_list:
    unknown_word.append('_')
print(random_word)
print('The answer so far is ' + ' '.join(unknown_word))

while tries != 0 and ''.join(unknown_word) != random_word: 
    
    #   - prompt user to guess a letter and display remaining guesses
    player_guess = input('Guess a letter (' + str(tries) + ' guesses remaining): ').lower()
    
    # check to see if player guess has been made before
    repeat_guess = False
    for letter in guessed_letters:
        if letter == player_guess:
            tries = tries - 1
            repeat_guess = True
    guessed_letters.add(player_guess)
    
    # check and replace any matching letters in word with player guess
    index = -1
    no_match = True
    for letter in character_list:
        index = index + 1
        if player_guess == letter:
            unknown_word[index] = letter
            no_match = False
    if no_match == True and repeat_guess == False:
        tries = tries - 1
    # print remaining characters in the word
    print('The answer so far is ' + ' '.join(unknown_word))
    
# if player guesses the correct word display contratulations message
#   - if player does not correctly guess after 4 guess display condolensce

if tries == 0:
    print ('Not quite, the correct word was ' + random_word + '. Better luck next time')
else:
    print('Good job! You found the word ' + random_word)
input('Press enter to end the game.')