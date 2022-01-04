# Coin Toss Game

import random

# keeps track of total session scores
total_scores = {
    'ties': 0,
    'player_1': 0,
    'player_2': 0
}

def instructions():
    # prints instructions from txt file
    filename = 'instructions.txt'
    filemode = 'r'
    file = open(filename,filemode)
    instructions = file.read()
    file.close()
    print(instructions)

def toss():
    # function to randomly output H or T
    coin = ['H','T']
    flip = random.choice(coin)
    return flip

def player_toss(player):
    # prints what player tossed and returns toss value
    player_toss = toss()
    print(player+' has tossed '+player_toss)
    return player_toss

def toss_winner(player,toss,choice):  
    # prints whether player won the toss
    if toss == choice:
        print(player+' wins')
        return 1
    else:
        return 0
    
def round_winner(first_score,second_score):
    # prints and returns round winner
    winner = ''
    if first_score == second_score:
        print('The score was a tie')
        winner = 'tie'
    elif first_score > second_score:
        print('Player 1 wins this round')
        winner = 'Player 1'
    else:
        print('Player 1 wins this round')
        winner = 'Player 2'
    return winner
    
def hh_sequence(player,player_tosses):
    # checks for adjecent H H sequence in tosses list
    last = 'nil'
    hh_counter = 0
    for element in player_tosses:
        if element == last and element == 'H':
            hh_counter = hh_counter + 1
        last = element
    print('H H found in the '+player+' sequence ' + str(hh_counter) + ' times')         
        
def round_results(player_one_score,player_two_score):
    # prints round results
    round_win = ''
    print('ROUND STATS')
    round_win = round_winner(player_one_score,player_two_score)
    print('Player 1 points '+str(player_one_score))
    print('Player 2 points '+str(player_two_score))    
    return round_win

def play_round():
    # performs main game functions and prints round results
    flips = 1
    player_one_score = 0
    player_two_score = 0
    player_one_tosses = []
    player_two_tosses = []
    # prompts user for input and performs player turns
    while flips < 5:
        user_choice = input('Heads or Tails ? Type H or T >').upper()
        player_one_tosses.append(player_toss('Player 1'))
        player_two_tosses.append(player_toss('Player 2'))
        player_one_score = player_one_score + toss_winner('Player 1',player_one_tosses[-1],user_choice)
        player_two_score = player_two_score + toss_winner('Player 2',player_two_tosses[-1],user_choice)
        flips = flips + 1
    # prints round results
    round_winner = round_results(player_one_score,player_two_score)
    # prints additional data on round
    print('Player 1 tossed '+str(player_one_tosses))
    print('Player 2 tossed '+str(player_two_tosses))
    hh_sequence('Player 1',player_one_tosses)
    hh_sequence('Player 2',player_two_tosses)
    return round_winner

def session_scores(current_stats,round_winner):
    # tallies up total session scores
    if round_winner == 'tie':
        current_stats['ties'] = current_stats['ties'] + 1
    elif round_winner == 'Player 1':
        current_stats['player_1'] = current_stats['player_1'] + 1
    elif round_winner == 'Player 2':
        current_stats['player_2'] = current_stats['player_2'] + 1
    return current_stats
        
def play_again(scores):
    # prompts user to restart game
    # if no, prints session stats
    play_again = input('Do you want to play another round? y/n >')
    if play_again.lower() == 'y':
        main()
    else:
        print('SUMMARY STATS')
        print('number of ties '+str(scores['ties']))
        print('number of player 1 wins '+str(scores['player_1']))
        print('number of player 2 wins '+str(scores['player_2']))

def main():
    # progresses through main game functions
    instructions()
    winner = play_round()
    scores=session_scores(total_scores,winner)
    play_again(scores)

main()