# Coin Toss Game
#   -user decides heads or tails
#   -two computer players flip a coin 4 times
#   -if flip matches user choice player gets a point
#   -after 4 flips player with highest points wins

# import random module
import random

def instructions():
    # prints instructions from txt file
    filename = 'instructions.txt'
    filemode = 'r'
    file = open(filename,filemode)
    instructions = file.read()
    file.close()
    print(instructions)

def toss():
    # randomly outputs H or T
    coin = ['H','T']
    flip = random.choice(coin)
    return flip

def player_toss(player):
    # prints what player tossed and returns toss value
    # player parameter is type str and contains player name
    player_toss = toss()
    print(player+' has tossed '+player_toss)
    return player_toss

def toss_winner(player,toss,choice):  
    # prints whether player won the toss
    # player parameter is type str and contains player name
    # toss parameter is type str and contains result of coin toss
    # choice parameter is type str and contains user choice of H or T
    if toss == choice:
        print(player+' wins')
        return 1
    else:
        return 0
    
def round_winner(first_score,second_score):
    # determines and returns round winner
    # both parameters are int type and contain tallied scores of player for the round
    winner = str()
    if first_score == second_score:
        print('The score was a tie')
        winner = 'tie'
    elif first_score > second_score:
        print('Player 1 wins this round')
        winner = 'Player 1'
    else:
        print('Player 2 wins this round')
        winner = 'Player 2'
    return winner
    
def hh_sequence(player,player_tosses):
    # checks for adjecent H H sequence in tosses list
    # player parameter is type str and contains player name
    # player_tosses is type list and contains sequence of player tosses for the round
    last = str()
    hh_counter = 0
    for element in player_tosses:
        if element == last and element == 'H':
            hh_counter = hh_counter + 1
        last = element
    print('H H found in the '+player+' sequence ' + str(hh_counter) + ' times')         
        
def round_results(player_one_score,player_two_score):
    # prints round results
    # both parameters are type int and contain tallied scores of player for the round
    round_win = str()
    print('ROUND STATS')
    round_win = round_winner(player_one_score,player_two_score)
    print('Player 1 points '+str(player_one_score))
    print('Player 2 points '+str(player_two_score))    
    return round_win

def play_round():
    # performs main game functions and prints round results
    flips = 1
    player_one_score,player_two_score = 0,0
    player_one_tosses,player_two_tosses = [],[]
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
    additional_data(player_one_tosses,player_two_tosses)
    return round_winner

def additional_data(toss_one,toss_two):
    # prints additional data about round
    # both parameter are type list and contain sequence of player tosses for the round
    print('Player 1 tossed '+str(toss_one))
    print('Player 2 tossed '+str(toss_two))
    hh_sequence('Player 1',toss_one)
    hh_sequence('Player 2',toss_two)
        
def game_loop(initial_scores):
    # calls most main functions in appropriate order and ask if player would like to replay
    # initial_scores is type dict and is used to bring in initial session scores of 0
    play_again = 'y'
    scores = initial_scores
    while play_again.lower() == 'y':
        instructions()
        winner = play_round()
        scores = session_scores(scores,winner)        
        play_again = input('Do you want to play another round? y/n >')
    return scores

def session_scores(current_score,round_winner):
    # tallies up total session scores
    # current_score parameter type dict, contains current sessions scores
    # round_winner parameter type dict, contains last round scores
    if round_winner == 'tie':
        current_score['ties'] = current_score['ties'] + 1
    elif round_winner == 'Player 1':
        current_score['player_1'] = current_score['player_1'] + 1
    elif round_winner == 'Player 2':
        current_score['player_2'] = current_score['player_2'] + 1
    return current_score

def session_summary(scores):
    # prints round summary stats
    # scores is type dict and contains total session scores
    print('SUMMARY STATS')
    print('number of ties '+str(scores['ties']))
    print('number of player 1 wins '+str(scores['player_1']))
    print('number of player 2 wins '+str(scores['player_2']))

def main():
    # defines initial total scores variable and passes into play function to start game
    total_scores = {
        'ties': 0,
        'player_1': 0,
        'player_2': 0
    }    
    session_scores = game_loop(total_scores)
    session_summary(session_scores)
    
main()