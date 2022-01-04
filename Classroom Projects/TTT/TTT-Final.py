# TTT Version 2 - Two Player game

import pygame


# User-defined functions

def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Tic Tac Toe')   
   # get the display surface
   w_surface = pygame.display.get_surface() 
   # create a game object
   game = Game(w_surface)
   # start the main game loop by calling the play method on the game object
   game.play() 
   # quit pygame and clean up the pygame window
   pygame.quit() 


# User-defined classes

class Game:
   # An object in this class represents a complete game.

   def __init__(self, surface):
      # Initialize a Game.
      # - self is the Game to initialize
      # - surface is the display window surface object

      # === objects that are part of every game that we will discuss
      self.surface = surface
      self.bg_color = pygame.Color('black')
      
      self.FPS = 60
      self.game_Clock = pygame.time.Clock()
      self.close_clicked = False
      self.continue_game = True
      
      # === game specific objects
      self.board_size = 3
      self.player_1 = 'X'
      self.player_2 = 'O'
      self.turn = self.player_1 
      self.board = [] # will be rpresent by a list of lists (aka a matrix)
      self.stop_color = pygame.Color('red')
      self.colored = []
      self.filled = []
      self.create_board()
      
   def create_board(self):
      width = self.surface.get_width()//self.board_size
      height = self.surface.get_height()//self.board_size
      for row_index in range(0,self.board_size):
         row = []
         for col_index in range(0,self.board_size):
            x = col_index*width
            y = row_index*height
            tile = Tile(x,y,width,height,self.surface)
            row.append(tile)
         self.board.append(row)
      
   def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game that should be continued or not.

      while not self.close_clicked:  # until player clicks close box
         # play frame
         self.handle_events()
         self.draw()            
         if self.continue_game:
            self.update()
            self.decide_continue()
         self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second 

   def handle_events(self):
      # Handle each user event by changing the game state appropriately.
      # - self is the Game whose events will be handled

      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked = True
         if event.type == pygame.MOUSEBUTTONUP and self.continue_game:
            self.handle_mouse_up(event.pos) # event.pos is (x,y) tuple ---> position of the click
   
   def handle_mouse_up(self,position):
      # - position is the location where the click happened
      for row in self.board:
         for tile in row:
            if tile.select(position,self.turn): # select method is in the Tile class
               self.filled.append(tile)
               self.change_turn()
   
   def change_turn(self):
      if self.turn == self.player_1:
         self.turn = self.player_2
      else:
         self.turn = self.player_1

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.surface.fill(self.bg_color) # clear the display surface first
      if self.continue_game == False: # end of game condition
         for tile in self.colored:
            # each tile in self colored should turn red
            tile.set_color(self.stop_color)
      # draw the board
      for row in self.board:
         for tile in row:
            tile.draw()
      pygame.display.update() # make the updated surface appear on the display

   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      pass
   
   def is_row_win(self):
      row_win = False
      list_of_lists_of_tiles = self.board
      if self.contains_list_win(list_of_lists_of_tiles):
         row_win = True
      return row_win
   
   def is_col_win(self):
      # collect all the columns that are in the board and put these inside a list list_of_lists_of_tiles
      col_win = False
      list_of_lists_of_tiles = []
      for col_index in range(0,self.board_size):
         column = []
         for row_index in range(0,self.board_size):
            tile = self.board[row_index][col_index]
            column.append(tile)
         list_of_lists_of_tiles.append(column)
      if self.contains_list_win(list_of_lists_of_tiles):
         col_win = True
      return col_win
   
   def is_diagonal_win(self):
      # collect all the diagonal diagonals that are in the board and put these inside a list list_of_lists_of_tiles
      diag_win = False
      list_of_lists_of_tiles = []
      red = []
      green = []
      for index in range(0,self.board_size):
         tile = self.board[index][index]
         red.append(tile)
         tile = self.board[index][self.board_size-1-index]
         green.append(tile)
      list_of_lists_of_tiles.append(red)
      list_of_lists_of_tiles.append(green)
      if self.contains_list_win(list_of_lists_of_tiles):
         diag_win = True
      return diag_win         
   
   def contains_list_win(self,list_of_lists_of_tiles):
      # list_of_list_of_tiles ----> [[T0,T1,T2],[T3,T4,T5],[T6,T7,T8]]
      list_win = False
      for list_of_tiles in list_of_lists_of_tiles:
         # list_of_tiles ---> [T0,T1,T2]
         if self.is_list_win(list_of_tiles):
            list_win = True
      return list_win
   
   def is_list_win(self, list_of_tiles): # [T0,T1,T2]
      same = True
      first = list_of_tiles[0]
      for tile in list_of_tiles:
         # important for memory
         if not first.is_equal(tile):
            same = False
      if same:
         for tile in list_of_tiles:
            self.colored.append(tile)
      return same
         
   def is_win(self):
      win = False
      row_win = self.is_row_win()
      col_win = self.is_col_win()
      diagonal_win = self.is_diagonal_win()
      if row_win or col_win or diagonal_win:
         win = True
      return win
      
   def is_tie(self):
      tie = False
      if  len(self.filled) == self.board_size**2:
         tie = True
         self.colored = self.filled
      return tie
         
   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      
      if self.is_win() or self.is_tie():
         self.continue_game = False

class Tile:
   # A class is a blueprint ----> properties and behaviour
   
   def __init__(self,x,y,width,height,surface):
      self.rect = pygame.Rect(x,y,width,height)
      self.color = pygame.Color('white')
      self.border_width = 3
      self.content = ''
      self.flashing = False # self.hidden = True
      self.surface = surface
   
   def set_color(self,new_color):
      self.color = new_color
      
   def is_equal(self,other):
      if self.content != '' and self.content == other.content:
         return True
      else:
         return False
      
   def select(self,position,current_player):
      # handle_mouse_up method in the Game class calls this method
      # position is the (x,y) of the location of the click
      # current player is of type string
      selected = False
      if self.rect.collidepoint(position):
         if self.content == '':
            self.content = current_player
            selected = True
         else:
            self.flashing = True
      return selected
   
   def draw(self):
      # draw the coordinates of each Tile objects
      #string = str(self.rect.x)+','+str(self.rect.y)
      #font = pygame.font.SysFont('',40)
      #text_box = font.render(string,True,self.color)
      #location = (self.rect.x,self.rect.y)
      #self.surface.blit(text_box,location)
      if self.flashing:
         # draw a white rectangle
         pygame.draw.rect(self.surface,self.color,self.rect,0)
         self.flashing = False
      else:
         # draw a rectangle with a white border
         pygame.draw.rect(self.surface,self.color,self.rect,self.border_width)
      self.draw_content()
      
   def draw_content(self):
      font = pygame.font.SysFont('',133) # height of the surface is 400//3
      text_box = font.render(self.content,True,self.color)
      # text_box = is a pygame.Surface object - get the rectangle from the surface
      rect1 = text_box.get_rect()
      rect1.center = self.rect.center
      location = (rect1.x,rect1.y)
      self.surface.blit(text_box,location)
      
main()