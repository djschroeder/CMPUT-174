# Race Game
# Two players roll a dice and see who can land on the eighth position first

import random

def roll_die():
    # returns a random number from 1-6
    return random.randint(1,6)

def display_state(lane):
    # displays updated game lane
    # lane is type list and represents the game track
    border = '*' * 36
    print(border)
    print('update: '+' '.join(lane))
    print(border)
  
def update_position(lane,player,roll):
    # updates player position on the lane
    # lane is type list and represents the game track
    # player is type str and contains the player symbol
    # roll is type int and contains the dice roll for the round
    if player in lane: 
        # this if statement is to prevent an error when the .index() 
        #   method below doesnt detect a 'x' in the list on the first round
        current_position = lane.index(player) 
        updated_position = current_position + roll
    if lane[0] == '*':
        # this if statement only executes during the first round
        lane[roll] = player
        lane[0] = opponent(player)
    elif (updated_position) <= (len(lane) - 1):
        # this if statement updates player position for most rounds
        lane[current_position] = '-'
        if lane[updated_position] == opponent(player):
            # this if statement determines if a player is kicked back to the start
            lane[0] = opponent(player)
            print(player+' kicked the rival!')
        lane[updated_position] = player
    else:
        print('The roll was too high, player '+player+' stays in this position')
    # updated lane list does not need to be returned as it is an iterable object
    
def check_game_over(player,lane):
    # determines if a player has reached the last spot in the line
    # if there is a winner, returns true to stop the primary game while loop from continuing
    # player is type str and contains the player symbol
    # lane is type list and represents the game track
    if lane[-1] == player:
        print('Player '+player+' has won!')
        return True

def opponent(player):
    # determines the opposing player the one supplied as the arguement
    # player is type str and contains the player symbol
    player_x = 'x'
    player_o = 'o'
    if player == player_x:
        return player_o
    elif player == player_o:
        return player_x
    
def main():
    # establishes initial game values and commences game loop
    print('Players begin in the starting position')
    current_player = 'x'
    lane = ['*']+['-']*7
    display_state(lane)
    game_over = False
    while not game_over:
        input('Player '+current_player+' press enter to roll!')
        dice_roll = roll_die()
        print('Player '+current_player+' rolled a '+str(dice_roll))
        update_position(lane,current_player,dice_roll)
        display_state(lane)
        game_over = check_game_over(current_player,lane)
        current_player = opponent(current_player)
    
main()