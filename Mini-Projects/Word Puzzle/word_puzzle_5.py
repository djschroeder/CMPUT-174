# Word Puzzle Game
#   - word is randomly selected from word list
#   - player tries to guess the word one letter at a time
#   - after four guesses or upon guessing correct answer game ends

#import random module
import random

def instructions():
    # prints instructions for game from external file
    filename = 'wp_instructions.txt'
    filemode = 'r'
    infile = open(filename,filemode)
    instructions = infile.read()
    infile.close()
    print(instructions)

def random_word():
    # chooses word randomly from words list
    word_list = ['apple','banana','watermelon','kiwi','pineapple','mango']
    random_word = random.choice(word_list)
    return random_word

def blank_word(character_list):
    # generates unknown character list
    # character_list is type list and contains list of characters from selected word
    unknown_word = []
    for character in character_list:
        unknown_word.append('_')
    print('The answer so far is ' + ' '.join(unknown_word))
    return unknown_word
    
def update_word(character_list,player_guess,unknown_word):
    # updates unknown word
    # character_list is type list and contains list of characters from selected word
    # player_guess is type str and contains player letter guess
    # unknown_word is type list and contains current unknown state of word amended with player letter guesses
    index = -1
    updated_word = list(unknown_word)  # copy list to avoid changing original list object
    for letter in character_list:
        index = index + 1
        if player_guess == letter:
            updated_word[index] = letter
    return updated_word

def match_test(updated_word,unknown_word):
    # determines if player guess is in the word
    # updated_word is type list and contains unknown_word updated with last guess
    # unknown_word is type list and contains is the previous state of unknown word
    no_match = False
    if updated_word == unknown_word:
        no_match = True
    else:
        unknown_word = unknown_word
    return no_match

def repeat_test(guessed_letters,player_guess):        
    # determines if player guess is a repeat
    # guessed_letters is type set and contains previously guessed letters
    # player_guess is type str and contains player letter guess
    repeat_guess = False
    for letter in guessed_letters:
        if letter == player_guess:
            repeat_guess = True
    guessed_letters.add(player_guess)
    return repeat_guess

def attempts(current_tries,repeat_guess,no_match):
    # determines remaining attempts
    # current tries is type int and contains remaining attempts
    # repeat_guess is type bool and indicates whether there was a repeat guess
    # no_match is type bool and indicates whether there was no match for player guess
    if repeat_guess == True or no_match == True:
        current_tries = current_tries - 1
    return current_tries
    
def run_game(selected_word,character_list,guessed_letters):
    # performs main game loop
    # selected_word is type str and contains the randomly chosen word
    # character_list is type list and contains list of characters from selected word
    # guessed_letters is type set and contains previously guessed letters
    tries = 4   
    unknown_word = blank_word(character_list)
    # while loop repeats until user runs out of tries or successfully guesses word
    while tries != 0 and ''.join(unknown_word) != selected_word:
        # prompts user to guess a letter and displays remaining guesses
        player_guess = input('Guess a letter (' + str(tries) + ' guesses remaining): ').lower()
        # checks if player guess was a repeat guess
        repeat_result = repeat_test(guessed_letters,player_guess)
        # creates updated word including last player guess
        updated_word = update_word(character_list,player_guess,unknown_word)
        # checks whether updated word and previous unknown word state match
        match_result = match_test(updated_word,unknown_word)
        # updates unknown word to the uptdated word
        unknown_word = updated_word
        # updates remaining attempts 
        tries = attempts(tries,repeat_result,match_result)
        # print remaining characters in the word
        print('The answer so far is ' + ' '.join(unknown_word))
    return tries

def game_over(tries, selected_word):
    # deternubes and prints player game result
    # tries is type int and contains remaining attempts
    # selected_word is type str and contains the randomly chosen word
    if tries == 0:
        print ('Not quite, the correct word was ' + selected_word + '. Better luck next time')
    else:
        print('Good job! You found the word ' + selected_word + '!')
    input('Press enter to end the game.')
    
def main():
    # executes primary function sequence
    guessed_letters = set()
    instructions()
    selected_word = random_word()
    character_list = list(selected_word)
    tries_remaining = run_game(selected_word,character_list,guessed_letters)
    game_over(tries_remaining,selected_word)    

main()
