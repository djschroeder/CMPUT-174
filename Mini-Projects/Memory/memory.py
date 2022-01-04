# Memory - player tries to remember and match pairs of tiles


import pygame, random

def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Memory')   
   # get the display surface
   w_surface = pygame.display.get_surface() 
   # create a game object
   game = Game(w_surface)
   # start the main game loop by calling the play method on the game object
   game.play() 
   # quit pygame and clean up the pygame window
   pygame.quit() 

class Game:
   # An object in this class represents a complete game.
   
   def __init__(self, surface):
      # Initialize a Game.
      # - self is the Game to initialize
      # - surface is the display window surface object
      self.surface = surface
      self.bg_color = pygame.Color('black')
      self.FPS = 60
      self.game_Clock = pygame.time.Clock()
      self.close_clicked = False
      self.continue_game = True
      
      # === game specific objects
      self.first_selection = None
      self.second_selection = None
      self.score = 0
      self.board_size = 4
      self.image_list = []
      self.load_images()
      self.image_list = self.randomize_image_list()
      self.board = [] # will be rpresent by a list of lists (aka a matrix)
      self.create_board()
   
   def load_images(self):
      # loads all the memory images and adds them to a list
      # - self is the Game that the images are being generated for
      image1 = pygame.image.load('image1.bmp')
      self.image_list.append(image1)
      image2 = pygame.image.load('image2.bmp')
      self.image_list.append(image2)
      image3 = pygame.image.load('image3.bmp')
      self.image_list.append(image3)
      image4 = pygame.image.load('image4.bmp')
      self.image_list.append(image4)
      image5 = pygame.image.load('image5.bmp')
      self.image_list.append(image5)
      image6 = pygame.image.load('image6.bmp')
      self.image_list.append(image6)
      image7 = pygame.image.load('image7.bmp')
      self.image_list.append(image7)
      image8 = pygame.image.load('image8.bmp')
      self.image_list.append(image8)
      
   def randomize_image_list(self):
      # doubles and shuffles the image list
      # - self is the Game whose images are being randomized
      image_list = self.image_list*2
      random.shuffle(image_list)
      return image_list
   
   def create_board(self):
      # creates the game board
      # - self is the Game whose board is being generated
      #width = self.surface.get_width()//self.board_size
      #height = self.surface.get_height()//self.board_size
      image_index = -1
      for row_index in range(0,self.board_size):
         row = []
         for col_index in range(0,self.board_size):
            image_index = image_index+1
            image = self.image_list[image_index]
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
         if event.type == pygame.MOUSEBUTTONUP and self.continue_game:
            self.handle_mouse_up(event.pos) # event.pos is (x,y) tuple ---> position of the click
   
   def handle_mouse_up(self,position):
      # Handles mouse up events
      # - self is the Game whose mouse up events are being handled
      # - position is the location where the click happened and is type tuple
      for row in self.board:
         for tile in row:
            selected = tile.select(position) # select method is in the Tile class
            if selected and not tile.already_matched():
               self.selections(tile)
            
   def selections(self,selection):
      # Determines whether player selection was the first or second selection of the pair
      # - self is the Game which is having tiles selected by the player
      # - selection is the tile of Tile class that the player picked
      if self.first_selection == None:
         self.first_selection = selection
      elif self.first_selection.get_location() != selection.get_location():
         self.second_selection = selection
      
   def check_match(self):
      # determines if there is a match between two tiles
      # - self is the Game which is being checked for matches
      if self.first_selection.get_content() == self.second_selection.get_content():
         self.match()
         self.clear_selections()
      else:
         pygame.time.delay(1000)
         self.first_selection.set_hidden()
         self.second_selection.set_hidden()
         self.clear_selections()
      
   def match(self):
      # if there is a match, sets the tile mode to matched
      # - self is the Game which is having tiles set to matching
      self.first_selection.match()
      self.second_selection.match()
   
   def clear_selections(self):
      # clears player selections
      # - self is the Game whose player selections are being cleared
      self.first_selection = None
      self.second_selection = None
      
   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      self.surface.fill(self.bg_color) # clear the display surface first
      # draw the board
      for row in self.board:
         for tile in row:
            tile.draw()
      self.draw_score(self.score)
      pygame.display.update() # make the updated surface appear on the display

   def draw_score(self,score):
      # draws the player score
      # - self is the Game whose score is being drawn
      # - score is the time in seconds that have passed and is type int
      font_size = 80
      fg_color = pygame.Color('white')
      font = pygame.font.SysFont('', font_size)
      text_box = font.render(str(score), True, fg_color, self.bg_color)
      x = self.surface.get_width()-text_box.get_width()
      y = 0
      location = (x,y)
      self.surface.blit(text_box,location)
   
   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      self.score = pygame.time.get_ticks()//1000
      if (self.first_selection and self.second_selection) != None:
         self.check_match()
   
   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      self.continue_game = False
      for row in self.board:
         for tile in row:
            if not tile.already_matched():
               self.continue_game = True

class Tile:
   # An object of this Class represents one of 16 game tiles
   
   def __init__(self,x,y,width,height,image,surface):
      # initializes a tile
      # - self is the tile that is being initialized
      # - x and y are type int and give the tile location
      # - width and hight are type int and give the tile size
      # - image is type pygame.Surface and is the content image
      # - surface is type pygame.Surface and is the game window surface
      self.rect = pygame.Rect(x,y,width,height)
      self.color = pygame.Color('white')
      self.border_width = 3
      self.surface = surface
      self.content = image
      self.hidden = True
      self.hidden_image = pygame.image.load('image0.bmp')
      self.paired = False
      self.location = (x,y)
   
   def already_matched(self):
      # returns if the tile has already been paired
      # - self is the Tile whose pair status is being requested
      return self.paired
   
   def match(self):
      # updates the Tiles pair status
      # - self is the Tile whose pair status is being updated
      self.paired = True
   
   def get_content(self):
      # returns the Tiles content
      # - self is the Tile whose content is being requested
      return self.content
   
   def set_hidden(self):
      # sets the tile to hidden
      # - self is the Tile that is being set to hidden
      self.hidden = True
   
   def get_location(self):
      # returns the tiles location
      # - self is the Tile whose location is being requested
      return self.location
   
   def select(self,position):
      # determines if the Tile has been selected by the player
      # handle_mouse_up method in the Game class calls this method
      # - position is the (x,y) of the location of the click
      # - current player is of type string
      selected = False
      if self.rect.collidepoint(position):
         self.hidden = False
         selected = True
      return selected   
   
   def draw(self):
      # draws the tile object to the Game surface
      # - self is the Tile that is being drawn
      location = (self.rect.x,self.rect.y)
      if self.hidden == True:
         self.surface.blit(self.hidden_image,location)
      else:
         self.surface.blit(self.content,location)
      pygame.draw.rect(self.surface,self.color,self.rect,self.border_width)

   def draw_content(self):
      # draws Tile content onto the Tile surface
      # - self is the Tile which is having its content drawn
      font = pygame.font.SysFont('',133) # height of the surface is 400//3
      text_box = font.render(self.content,True,self.color)
      # text_box = is a pygame.Surface object - get the rectangle from the surface
      rect1 = text_box.get_rect()
      rect1.center = self.rect.center
      location = (rect1.x,rect1.y)
      self.surface.blit(text_box,location)
      
main()