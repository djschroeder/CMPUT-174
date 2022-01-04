# Word Puzzle Game

import random

def instructions():
    # display instructions
    filename = 'wp_instructions.txt'
    filemode = 'r'
    infile = open(filename,filemode)
    instructions = infile.read()
    infile.close()
    print(instructions)

def random_word():
    # choose word randomly from words list
    word_list = ['apple','banana','watermelon','kiwi','pineapple','mango']
    random_word = random.choice(word_list)
    return random_word

def game_over(tries, selected_word):
    # if player guesses the correct word display contratulations message
    #   - if player does not correctly guess after 4 guess display condolensce
    if tries == 0:
        print ('Not quite, the correct word was ' + selected_word + '. Better luck next time')
    else:
        print('Good job! You found the word ' + selected_word)
    input('Press enter to end the game.')
    
def update_word(character_list,player_guess,unknown_word):
    # check and replace any matching letters in word with player guess
    index = -1
    for letter in character_list:
        index = index + 1
        if player_guess == letter:
            unknown_word[index] = letter
    return unknown_word

def main():
    instructions()
    selected_word = random_word()
    
    
    # variables
    guessed_letters = set()
    tries = 4
    
    character_list = list(selected_word)    
    unknown_word = []
    for character in character_list:
        unknown_word.append('_')
    print('The answer so far is ' + ' '.join(unknown_word))
    
    while tries != 0 and ''.join(unknown_word) != selected_word: 
        
        #   - prompt user to guess a letter and display remaining guesses
        player_guess = input('Guess a letter (' + str(tries) + ' guesses remaining): ').lower()
        
        # check to see if player guess has been made before
        repeat_guess = False
        for letter in guessed_letters:
            if letter == player_guess:
                tries = tries - 1
                repeat_guess = True
        guessed_letters.add(player_guess)
    
        unknown_word = update_word(character_list,player_guess,unknown_word)
    
        if repeat_guess == False: #and no_match == True
            tries = tries - 1
        # print remaining characters in the word
        print('The answer so far is ' + ' '.join(unknown_word))
    
    game_over(tries,selected_word)

    

main()
