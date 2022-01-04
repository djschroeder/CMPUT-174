# Cards Game
#   - two players draw hands of five cards, player with most aces wins
#   - if there its a tie, game restarts

import random

class Card:
    # An object of this class represents a single card
    def __init__(self,rank,suit):
        # Initializes a card
        # rank is type int and falls between 1-13
        # suit is type str and indicates the suit of the card
        self.rank = rank
        self.suit = suit
    def get_rank(self):
        # returns the rank int of the card object
        return self.rank
    def display(self):
        # prints the rank and suit of the card object as a string
        rank_names = ['Ace','Two','Three','Four','Five','Six','Seven',
                      'Eight','Nine','Ten','Jack','Queen','King']
        for rank in rank_names:
            if self.rank == rank_names.index(rank) + 1:
                print(rank+' of '+self.suit)

class Deck:
    # An object of this class represents a deck of 52 unique cards arranged in a list
    def __init__(self):
        # Initalizes a deck via a list of 52 card objects
        self.suit = ['Clubs','Diamonds','Hearts','Spades']
        self.rank = list(range(1,14))     
        self.cards = []
        for suit in self.suit:
            for rank in self.rank:
                self.cards.append(Card(rank,suit))
    def shuffle(self):
        # randomly shuffles the order of the 52 card objects in the list
        random.shuffle(self.cards)
    def deal(self):
        # returns and removes the last card from the deck list
        return self.cards.pop()

class Player:
    # An object of this class represents an individual player
    def __init__(self):
        # initalizes a player
        self.hand = []
        self.aces = 0
    def add(self,card):
        # adds a card to the players hand from the deck
        # card is type Card and is the last card removed from the deck list
        self.hand.append(card)
    def ace_cards(self):
        # returns the number of aces in the players hand as an int
        for card in self.hand:
            if card.get_rank() == 1:
                self.aces = self.aces + 1
        return self.aces
    def display(self):
        # prints the cards in the players hand
        for card in self.hand:
            card.display()

def main():
    # performs main game sequence
    deck = Deck() # creates a deck
    deck.shuffle() # shuffles the deck
    players = [Player(),Player()] # creates two player objects in a list
    for player in players:
        # adds 5 card objects from the deck to each players hand and prints the hand
        for i in range(0,5):
            player.add(deck.deal())
        print('\nThis is the hand of player '+str(players.index(player)+1)+':')
        player.display()
    # prints the number of aces in each players hand
    print("\nNumber of ace cards in each player's hand:")
    for player in players:
        print('Player '+str(players.index(player)+1)+' has '+str(player.ace_cards())+' aces')
    # determines and prints the winner
    print('\nResult:')
    if players[0].ace_cards() > players[1].ace_cards():
        print('Player 1 is the winner')
    elif players[0].ace_cards() < players[1].ace_cards():
        print('Player 2 is the winner')
    else:
        # if there is a tie it this statement resets the game
        print('No winner, shuffle again')
        main()
        
main()
    
    