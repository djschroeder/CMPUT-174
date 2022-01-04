# Remember The Word Design Version 4 
#                                    - clear the screen
#                                    - conditional feedback
#                                    - identify and replace adjacent duplicate line groups with a for statement
#                                    - SW quality requirements
#                                      - identify any literal in our program that occur more than once
#                                      - bind that literal to an identifier
#                                      - replace that literal with the identifier
#                                    - random selection of 4 words from a list of words read from a file
#                                    - random selection of answer from the 4 words
#                                    - player can play the game multiple times

import time, os, random

continue_game = True
while continue_game:
    # clear screen
    clear_command = 'clear'
    if os.name == 'nt':
        clear_command = 'cls'
    os.system(clear_command)
    
    # display header
    header_border = '-' * 80
    header_content = 'Remember The Word'
    print(header_border)
    print(header_content)
    print(header_border)
    
    # display instructions
    filename = 'instructions.txt'
    file_mode = 'r'
    infile = open(filename,file_mode)
    content = infile.read()
    infile.close()
    print(content)
    
    # prompt player to press enter
    input('Press enter key to display the words.')
    
    # clear screen
    os.system(clear_command)
    
    # display header
    print(header_border)
    print(header_content)
    print(header_border)
    
    # display four words
    #   - display word one at a time
    #   - 1 sec pause before the word disappears and the next word appears
    #   - words are chosen randomly from a list
    #   - words start with different letters
    filename = 'words.txt'
    file_mode = 'r'
    infile = open(filename,file_mode)
    all_words = infile.read()
    infile.close()
    # to see true represention of the words with endlines: print(repr(all_words))
    all_words_list = all_words.splitlines()
    words = random.sample(all_words_list,4)
    
    # choose the random answer from the words
    answer = random.choice(words)
    start_letter = answer[0]
    pause_time_seconds = 1
    for word in words:
        print(word)
        time.sleep(pause_time_seconds)
        os.system(clear_command)
        print(header_border)
        print(header_content)
        print(header_border)
    
    # prompt player to enter a word that starts with a particular letter
    #   - answer is chosen randomly from the four words that are displayed
    #   - use first letter of answer to prompt player
    guess = input('What word begins with the letter ' + start_letter + '?')
    
    # evaluate answer
    if guess.lower() == answer.lower():
        # display feedback
        print('Congratulations, you are correct.')
    else:
        print('Sorry, you entered ' + guess + '.')
    print('The answer was ' + answer + '.')
    
    # prompt player to play again
    #    - program restarts if player chooses to play again
    #    - otherwise program terminates
    reply = input('Play again?y/N').lower()
    continue_game = reply == 'y'