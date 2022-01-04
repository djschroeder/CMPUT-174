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
      self.board_size = 4
      self.image_list = []
      self.load_images()
      self.board = [] # will be rpresent by a list of lists (aka a matrix)
      self.create_board()
   
   def load_images(self):
      # do the following steps 8 times for image 1 - image 8
      image = pygame.image.load('image1.bmp')
      self.image_list.append(image)
      
   def create_board(self):
      #width = self.surface.get_width()//self.board_size
      #height = self.surface.get_height()//self.board_size
      for row_index in range(0,self.board_size):
         row = []
         for col_index in range(0,self.board_size):
            image = self.image_list[0]
            width = image.get_width()
            height = image.get_height()
            x = col_index*width
            y = row_index*height
            tile = Tile(x,y,width,height,image,self.surface)
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

class Tile:
   # A class is a blueprint ----> properties and behaviour
   
   def __init__(self,x,y,width,height,image,surface):
      self.rect = pygame.Rect(x,y,width,height)
      self.color = pygame.Color('white')
      self.border_width = 3
      self.surface = surface
      self.content = image
      self.hidden = True
      self.hidden_image = pygame.image.load('image0.bmp')
      
   def draw(self):
      # draw the coordinates of each Tile objects
      #string = str(self.rect.x)+','+str(self.rect.y)
      #font = pygame.font.SysFont('',40)
      #text_box = font.render(string,True,self.color)
      #location = (self.rect.x,self.rect.y)
      #self.surface.blit(text_box,location)
      location = (self.rect.x,self.rect.y)
      if self.hidden == True:
         self.surface.blit(self.hidden_image,location)
      else:
         self.surface.blit(self.content,location)
      pygame.draw.rect(self.surface,self.color,self.rect,self.border_width)
      
      #self.draw_content()
   
   def draw_content(self):
      font = pygame.font.SysFont('',133) # height of the surface is 400//3
      text_box = font.render(self.content,True,self.color)
      # text_box = is a pygame.Surface object - get the rectangle from the surface
      rect1 = text_box.get_rect()
      rect1.center = self.rect.center
      location = (rect1.x,rect1.y)
      self.surface.blit(text_box,location)
main()