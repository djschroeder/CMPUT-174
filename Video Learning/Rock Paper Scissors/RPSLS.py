# Rock, Paper, Scissors, Lizard, Spock

import random


def main():
    rock = 'rock'
    paper = 'paper'
    scissors = 'scissors'
    lizard = 'lizard'
    spock = 'spock'
    computer_wins_msg = 'I win!'
    player_wins_msg = 'You win!'
    tie_msg = "It's a tie!"
    choices = [rock,paper,scissors,lizard,spock]
    
    wins_against = {scissors: [paper,lizard],
                    paper: [rock,spock],
                    rock: [lizard,scissors],
                    lizard: [spock,paper],
                    spock: [scissors,rock]
                    }
    
    computer_choice = random.choice(choices)
    print(computer_choice)
    player_choice =''
    while player_choice not in choices:
        player_choice = input('What do you choose: '+ ', '.join(choices) + '? >')
    
    if computer_choice in wins_against[player_choice]:
        print(player_wins_msg)
    elif player_choice in wins_against[computer_choice]:
        print(computer_wins_msg)
    else:
        print(tie_msg)
    
main()