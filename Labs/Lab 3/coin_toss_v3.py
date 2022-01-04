# Coin Toss Game Version 1

import random

# display instructions
filename = 'instructions.txt'
filemode = 'r'
file = open(filename,filemode)
instructions = file.read()
file.close()

# function to randomly output H or T
def toss():
    coin = ['H','T']
    flip = random.choice(coin)
    return flip

# create computer players
class player:
    def __init__(self, name, result, wins, tosses):
        self.name = name
        self.result = result
        self.wins = wins
        self.tosses = tosses
player_one = player('Player 1','none',0,[])
player_two = player('Player 2','none', 0,[])
players = [player_one,player_two]

# function displays round results
def round_result():
    print('ROUND STATS')
    #determines winner
    if players[0].wins == players[1].wins:
        print('The score was a tie')
    elif players[0].wins > players[1].wins:
        print(players[0].name + ' wins this round')
    else:
        print(players[1].name + ' wins this round')
    # calculates each players total wins
    for player in players:
        print(player.name + ' points ' + str(player.wins))
    # shows summary of individual player tosses
    for player in players:
        print(player.name + ' tossed ' + str(player.tosses))
    # determine the number of times HH is found in each players tosses
    for player in players:
        last = 'nil'
        hh_counter = 0
        for element in player.tosses:
            if element == last and element == 'H':
                hh_counter = hh_counter + 1
            last = element
        print('H H found in the ' + player.name + ' sequence ' + str(hh_counter) + ' times')
    
# this function runs the game
def play_game():
    # print instructions from external file
    print(instructions)
    # create 4 rounds
    for attempt in range(4):
        # prompt user to enter a call
        user_call = input('Heads or Tails ? Type H or T >')
        # randomly generate H or T for each of the computer players and provide feedback
        for player in players:
            toss_result = toss()
            player.result = toss_result
            player.tosses.append(toss_result)
            print(player.name + ' has tossed ' + player.result)
        for player in players:
            if player.result == user_call:
                player.wins = player.wins + 1
                print(player.name + ' wins')
       
# determines whether the user wants to play again
# if user selects no it prints back session stats
def play_again():
    restart = input('Do you want to play another round? y/n >')
    if restart == 'y':
        play_game()
    else:    
        print('number of ties ' + ties)
        for player in players:
            print('number of ' + player.name + ' wins ' + player.total_wins)

play_game()
round_result()
