# Coin Toss Game Version 1

import random

def instructions():
    # copy instructions from txt file
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

class player:
    # define player class
    def __init__(self,name,result,wins,total_wins,tosses):
        self.name = name
        self.result = result
        self.wins = wins
        self.total_wins = total_wins
        self.tosses = tosses
    def get_name (self):
        return self.name
    def set_result(self,result):
        self.result = result
    def get_result(self):
        return self.result
    def set_wins(self,wins):
        self.wins = wins
    def get_wins(self):
        return self.wins
    def set_total_wins(self,total_wins):
        self.total_wins = total_wins
    def get_total_wins(self):
        return self.total_wins
    def set_tosses(self,tosses):
        self.tosses.append(tosses)
    def get_tosses(self):
        return self.tosses
        
    
player_one = player('Player 1','none',0,0,[])
player_two = player('Player 2','none',0,0,[])
players = [player_one,player_two]

# global variable to track total ties
ties = 0

# func for resetting players round stats 
def reset_player():
    for player in players:
        player.set_result('none')
        player.set_wins(0)
        player.tosses = []

# this function runs the main portion of the game
def play_game():
    # print instructions from external file
    instructions()
    # create 4 rounds
    for guess in range(4):
        # prompt user to enter a call
        user_call = input('Heads or Tails ? Type H or T >')
        # randomly generate H or T for each of the computer players and provide feedback
        for player in players:
            toss_result = toss()
            player.set_result(toss_result)
            player.set_tosses(toss_result)
            print(player.get_name() + ' has tossed ' + player.get_result())
        for player in players:
            if player.get_result() == user_call:
                player.set_wins(player.get_wins() + 1)
                print(player.get_name() + ' wins')

# function displays round results
def round_result():
    print('ROUND STATS')
    #determines winner
    if players[0].get_wins() == players[1].get_wins():
        print('The score was a tie')
        global ties 
        ties = ties + 1
    elif players[0].get_wins() > players[1].get_wins():
        print(players[0].get_name() + ' wins this round')
        players[0].set_total_wins(players[0].get_total_wins + 1)
    else:
        print(players[1].get_name() + ' wins this round')
        players[1].total_wins = players[1].total_wins + 1    
    # calculates each players total round wins
    for player in players:
        print(player.get_name() + ' points ' + str(player.get_wins()))
    # shows summary of individual player tosses for round
    for player in players:
        print(player.get_name() + ' tossed ' + str(player.tosses))
    # determine the number of times HH is found in each players tosses
    for player in players:
        last = 'nil'
        hh_counter = 0
        for element in player.tosses:
            if element == last and element == 'H':
                hh_counter = hh_counter + 1
            last = element
        print('H H found in the ' + player.get_name() + ' sequence ' + str(hh_counter) + ' times')       

# determines whether the user wants to play again
# if user selects no it prints back session stats
def play_again():
    restart = input('Do you want to play another round? y/n >')
    if restart == 'y':
        reset_player()
        main()
    else:    
        print('SUMMARY STATS')
        print('number of ties ' + str(ties))
        print('number of player 1 wins ' + str(player_one.total_wins))
        print('number of player 2 wins ' + str(player_two.total_wins))

def main():
    play_game()
    round_result()
    play_again()
    
main()