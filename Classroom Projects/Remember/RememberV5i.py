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

def display_instructions():
    # displays instructions - side effect
    # returns None
    filename = 'instructions.txt'
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

def main():
    # main program
    continue_game = True
    while continue_game: 
        display_header()
        
        # display instructions
        display_instructions()
        
        # prompt player to press enter
        input('Press enter key to display the words.') # ignore the return object from the input function
        
        display_header()
        
        # sample four words
        words = sample_words()
        
        answer = random.choice(words)
        start_letter = answer[0]
        
        display_words(words)
        
        # prompt player to enter a word that starts with a particular letter
        #   - answer is chosen randomly from the four words that are displayed
        #   - use first letter of answer to prompt player
        guess = input('What word starts with the letter '+start_letter+'?')
        # evaluate answer and display feedback
        if guess.lower() == answer.lower():
            #   - congratulations message is displayed if player answers correctly
            print('Congratulations, you are correct.')
        else:
            #   - otherwise condolence message
            print('Sorry you entered '+guess+'.')
        print('The answer was '+answer+'.')
        # prompt player to play again
        #    - program restarts if player chooses to play again
        #    - otherwise program terminates
        reply = input('Play again?y/N').lower()
        continue_game = reply == 'y'

main()