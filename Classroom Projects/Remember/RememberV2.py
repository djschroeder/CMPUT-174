# Remember The Word Design Version 2 - display, prompt, pause, clear, conditional feedback, adjacent duplicate line groups with a for statement
import time, os
# clear screen
clear_command = 'clear'
if os.name == 'nt':
    clear_command = 'cls'
os.system(clear_command)
# display header
print('-' * 80)
print('Remember The Word')
print('-' * 80)

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
print('-' * 80)
print('Remember The Word')
print('-' * 80)    
# display four words
#   - display word one at a time
#   - 1 sec pause before the word disappears and the next word appears
#   - words are chosen randomly from a list
#   - words start with different letters
words = ['orange','chair','mouse','sandwich']
for word in words:
    print(word)
    time.sleep(1)
    os.system(clear_command)
    print('-' * 80)
    print('Remember The Word')
    print('-' * 80)    

# prompt player to enter a word that starts with a particular letter
#   - answer is chosen randomly from the four words that are displayed
#   - use first letter of answer to prompt player
guess = input('What word begins with the letter m?')

# evaluate answer
if guess == 'mouse':
    # display feedback
    print('Congratulations, you are correct.')
else:
    print('Sorry, you entered ' + guess + '.')
print('The answer was mouse.')
# prompt player to play again
#    - program restarts if player chooses to play again
#    - otherwise program terminates
input('Play again?y/N')