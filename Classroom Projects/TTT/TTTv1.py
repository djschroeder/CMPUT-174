# TTT Version 1

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
      # create board as an empty list
      self.board_size = 3
      self.board = []
      self.create_board()
      
   def create_board(self):
      width = self.surface.get_width()//3
      height = self.surface.get_height()//3
      # for each row index
      for row_index in range(0,self.board_size):
         # create row as an empty list
         row = []
         # for each column index
         for col_index in range(0,self.board_size):
            # create tile using row index and column index
            x = col_index * width 
            y = row_index * height
            tile = Tile(x,y,width,height,self.surface)
            # append tile to row
            row.append(tile)
         # append row to board
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

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.surface.fill(self.bg_color) # clear the display surface first
      # draw the board
      for row in self.board:
         for tile in row:
            tile.draw()
      pygame.display.update() # make the updated surface appear on the display

   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      pass
      

   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      pass
       

class Dot:
   # An object in this class represents a Dot that moves 
   
   def __init__(self, dot_color, dot_radius, dot_center, dot_velocity, surface):
      # Initialize a Dot.
      # - self is the Dot to initialize
      # - color is the pygame.Color of the dot
      # - center is a list containing the x and y int
      #   coords of the center of the dot
      # - radius is the int pixel radius of the dot
      # - velocity is a list containing the x and y components
      # - surface is the window's pygame.Surface object

      self.color = pygame.Color(dot_color)
      self.radius = dot_radius
      self.center = dot_center
      self.velocity = dot_velocity
      self.surface = surface
      
   def move(self):
      # Change the location of the Dot by adding the corresponding 
      # speed values to the x and y coordinate of its center
      # - self is the Dot
      
      for i in range(0,2):
         self.center[i] = (self.center[i] + self.velocity[i])
   
   def draw(self):
      # Draw the dot on the surface
      # - self is the Dot
      
      pygame.draw.circle(self.surface, self.color, self.center, self.radius)

class Tile:
   # an object of this class represents a Rectangular Tile
   
   def __init__(self, x, y, width, height,surface):
      
      # Initialize a tile to contain a ' '
      # - x is the int x coord of the upper left corner
      # - y is the int y coord of the upper left corner
      # - width is the int width of the tile
      # - height is the int height of the tile
      # - surface is pygame.Surface object on which a Tile object is drawn on
      
      self.rect = pygame.Rect(x,y,width,height)
      self.surface = surface
   
   def draw(self):
      # draws a Tile object
      # -self is the Tile object to draw
      color = pygame.Color('white')
      border_width = 3
      pygame.draw.rect(self.surface,color,self.rect,border_width)      

main()