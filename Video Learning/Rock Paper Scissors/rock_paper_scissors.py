# Rock, Paper, Scissors - "naive" implementation

# rock smashes scissors
# paper covers rock
# scissors cuts paper
import random


def main():
    rock = 'rock'
    paper = 'paper'
    scissors = 'scissors'
    computer_wins_msg = 'I win'
    player_wins_msg = 'You win!'
    tie_msg = "It's a tie!"
    choices = [rock,paper,scissors]
    computer_choice = random.choice(choices)
    print(computer_choice)
    player_choice =''
    while player_choice not in choices:
        player_choice = input('What do you choose: '+ ', '.join(choices) + '? >')
    if player_choice == rock:
        if computer_choice == paper:
            print(computer_wins_msg)
        elif computer_choice == scissors:
            print(player_wins_msg)
        else:
            print(tie_msg)
    if player_choice == paper:
        if computer_choice == scissors:
            print(computer_wins_msg)
        elif computer_choice == rock:
            print(player_wins_msg)
        else:
            print(tie_msg)
    if player_choice == scissors:
        if computer_choice == rock:
            print(computer_wins_msg)
        elif computer_choice == paper:
            print(player_wins_msg)
        else:
            print(tie_msg)
main()