# Pre-Poke Framework
# Implements a general game template for games with animation
# You must use this template for all your graphical lab assignments
# and you are only allowed to inlclude additional modules that are part of
# the Python Standard Library; no other modules are allowed

import pygame


# User-defined functions

def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500,400))
   # set the title of the display window
   pygame.display.set_caption('Pong 1.0')   
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
      self.ball = Ball('white', 5, [400, 50], [-2,1], self.surface)
      self.paddle_left = Paddle('white',3,75,0,10,40,self.surface)
      self.paddle_right = Paddle('white',3,425,0,10,40,self.surface)
      #self.max_frames = 150
      #self.frame_counter = 0

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
         if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            self.paddle_left.events(event)
            self.paddle_right.events(event)
        
   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.surface.fill(self.bg_color) # clear the display surface first
      self.ball.draw()
      self.paddle_left.draw()
      self.paddle_right.draw()
      pygame.display.update() # make the updated surface appear on the display

   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      self.ball.move()
      self.paddle_left.move()
      self.paddle_right.move()
      self.ball.collide(self.paddle_left)

   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      pass
      #if self.frame_counter > self.max_frames:
         #self.continue_game = False


class Ball:
   # An object in this class represents a ball that moves 
   
   def __init__(self, ball_color, ball_radius, ball_center, ball_velocity, surface):
      # Initialize a ball.
      # - self is the ball to initialize
      # - color is the pygame.Color of the ball
      # - center is a list containing the x and y int
      #   coords of the center of the ball
      # - radius is the int pixel radius of the ball
      # - velocity is a list containing the x and y components
      # - surface is the window's pygame.Surface object

      self.color = pygame.Color(ball_color)
      self.radius = ball_radius
      self.center = ball_center
      self.velocity = ball_velocity
      self.surface = surface
   
   def collide(self,paddle):
      if (self.center[0] - self.radius <= paddle.width):
         if (paddle.vpos < self.center[1] < paddle.vpos + paddle.height):
            self.velocity[0] = -self.velocity[0]
      
   def move(self):
      # Change the location of the ball by adding the corresponding 
      # speed values to the x and y coordinate of its center
      # - self is the ball
      size = self.surface.get_size()
      for i in range(0,2):
         self.center[i] = (self.center[i] + self.velocity[i])
         if self.center[i] < self.radius: # left or top edge
            self.velocity[i] = -self.velocity[i]
         if self.center[i] + self.radius > size[i]:
            self.velocity[i] = -self.velocity[i]
      
   def draw(self):
      # Draw the ball on the surface
      # - self is the ball
      pygame.draw.circle(self.surface, self.color, self.center, self.radius)

class Paddle:
   
   def __init__(self, rect_color, move_speed, horiz_pos, vert_pos, rect_width, rect_height, surface):
      self.color = rect_color
      self.width = rect_width
      self.height = rect_height
      self.surface = surface
      self.hpos = horiz_pos
      self.vpos = vert_pos
      self.down = False
      self.up = False
      self.speed = move_speed 
      
   def events(self,event):
      K_DOWN = 1073741905
      K_UP = 1073741906
      if event.type == pygame.KEYDOWN:
         if event.key == K_DOWN:
            self.down = True
         if event.key == K_UP:
            self.up = True 
      else:
         self.down = False
         self.up = False
         
   def move(self):
      height = self.surface.get_height()
      if self.down and self.vpos + self.height <= height:
         self.vpos = self.vpos + self.speed
      if self.up and self.vpos >= 0:
         self.vpos = self.vpos - self.speed
      
   def draw(self):
      pygame.draw.rect(self.surface,self.color,(self.hpos,self.vpos,self.width,self.height))
   
   
main()