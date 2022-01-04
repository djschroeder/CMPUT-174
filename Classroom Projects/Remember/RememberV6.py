# Remember The Word Version 1 Code - display, prompt, pause
# Remember Version 4 - clear the screen,
#                    - conditional feedback,
#                    - identify and replace adjacent duplicate line groups with a for statement 
#                    - Sw Quality Requirement
#                         - identify any literal in our program that occur more than once
#                         - bind that literal to an identifier
#                         - replace that literal with the identifier
#                    - random selection of 4 words from a list of words read from a file
#                    - random selection of answer from the 4 words
#                    - player can play the game multiple times 
# Remember Version 4
#                   - identify non-adjacent duplicate line groups
#                   - define a function and place the line group in the body of the function
#                   - replace multiple occurrences of the line group with a function
# Advantage of user defined functions - 1.6 - 
import time, os, random

def display_header():
    # clears the screen and displays the header
    clear_command = 'clear'
    if os.name == 'nt':
        clear_command = 'cls'
    os.system(clear_command)
    header_border = '-' * 80
    header_content = 'Remember The Word'
    print(header_border)
    print(header_content)
    print(header_border)    

def display_instructions(filename):
    # displays instructions - side effect
    # returns None
    file_mode = 'r'
    infile = open(filename,file_mode)
    content = infile.read() # read is a method call
    infile.close()
    print(content)    

def sample_words():
    # returns 4 randomly chosen words from a file
    filename = 'words.txt'
    file_mode = 'r'
    infile = open(filename, file_mode)
    all_words = infile.read()
    #print(repr(all_words))
    all_words_list = all_words.splitlines()
    #print(all_words_list)
    words = random.sample(all_words_list,4)    
    return words

def display_words(words):
    # display the words
    # - words is of type list
    pause_time = 1
    for word in words:
        print(word)
        time.sleep(pause_time)
        display_header()    
        
def prompt_for_guess(start_letter):
    #prompts the user to enter a word
    player_guess = input('What word starts with the letter '+start_letter+'?')
    return player_guess

def display_results(p_guess,answer):
    # evaluate answer and display results
    if p_guess.lower() == answer.lower():
        #   - congratulations message is displayed if player answers correctly
        print('Congratulations, you are correct.')
    else:
        #   - otherwise condolence message
        print('Sorry you entered '+p_guess+'.')
    print('The answer was '+answer+'.')
def prompt_to_continue():
    # prompt player to play again and returns the answer
    reply = input('Play again?y/N').lower()
    continue_game = reply == 'y'
    return continue_game

def main():
    # main program
    continue_game = True
    filename = 'instructions.txt'
    while continue_game: 
        # display header
        display_header()
        
        # display instructions
        display_instructions(filename)
        
        # prompt player to press enter
        input('Press enter key to display the words.') # ignore the return object from the input function
        
        # display header
        display_header()
        
        # sample words
        words = sample_words()
        # choose random answer and set start_letter
        answer = random.choice(words)
        start_letter = answer[0]
        
        #display words
        display_words(words)
        
        # prompt player to enter a word that starts with a particular letter
        guess = prompt_for_guess(start_letter) # start_letter is the argument
        
        # evaluate answer and display feedback
        display_results(guess,answer)
        continue_game = prompt_to_continue()
main()