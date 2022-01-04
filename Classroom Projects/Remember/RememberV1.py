# Remember The Word Design
import time
# clear screen
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
# display four words
#   - display word one at a time
#   - 1 sec pause before the word disappears and the next word appears
#   - words are chosen randomly from a list
#   - words start with different letters
print('orange')
time.sleep(1)
print('mouse')
time.sleep(1)
print('chair')
time.sleep(1)
print('sandwich')
time.sleep(1)

# prompt player to enter a word that starts with a particular letter
#   - answer is chosen randomly from the four words that are displayed
#   - use first letter of answer to prompt player
guess = input('What word begins with the letter c?')

# evaluate answer
# display feedback
#   - congratulations message is displayed if player answers correctly
#   - otherwise condolence message
print('Congratulations, you are correct.')
print('The answer was chair')
print('Sorry, you entered ' + guess + '.')
print('The answer was chair.')
# prompt player to play again
#    - program restarts if player chooses to play again
#    - otherwise program terminates
input('Play again?y/N')