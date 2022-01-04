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
   pygame.display.set_caption('Pong')   
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
      self.paddle_left = Paddle('white',3,75,180,10,40,self.surface)
      self.paddle_right = Paddle('white',3,425,180,10,40,self.surface)
      self.score_left = 0
      self.score_right = 0
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
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
               self.paddle_left.move_up()
            if event.key == pygame.K_a:
               self.paddle_left.move_down()
            if event.key == pygame.K_p:
               self.paddle_right.move_up()
            if event.key == pygame.K_l:
               self.paddle_right.move_down()            
         if event.type == pygame.KEYUP:
            if event.key == pygame.K_q or event.key == pygame.K_a:
               self.paddle_left.move_stop()
            if event.key == pygame.K_p or event.key == pygame.K_l:
               self.paddle_right.move_stop()
        
   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.surface.fill(self.bg_color) # clear the display surface first
      self.ball.draw()
      self.paddle_left.draw()
      self.paddle_right.draw()
      self.draw_score('left',self.score_left)
      self.draw_score('right',self.score_right)
      pygame.display.update() # make the updated surface appear on the display

   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      self.ball.move()
      self.paddle_left.move()
      self.paddle_right.move()
      self.ball.collide_left_paddle(self.paddle_left)
      self.ball.collide_right_paddle(self.paddle_right)
      
   def draw_score(self,side,score):
      score_string = str(score)
      font_size = 80
      fg_color = pygame.Color('white')
      font = pygame.font.SysFont('Times New Roman', font_size)
      text_box = font.render(score_string, True, fg_color, self.bg_color)
      if side == 'left':
         location = (0,0)
      elif side == 'right':
         location = (self.surface.get_width()-text_box.get_width(),0)
      self.surface.blit(text_box,location)   
      
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
   
   def collide_left_paddle(self,paddle):
      paddle_pos = paddle.get_pos() # self.vpos,self.height,self.hpos,self.width
      paddle_right = paddle_pos[2] + paddle_pos[3]
      paddle_top = paddle_pos[0]
      paddle_bottom = paddle_pos[0] + paddle_pos[1]
      if self.center[0] - self.radius == paddle_right and paddle_top < self.center[1] < paddle_bottom:
         if self.velocity[0] < 0:
            self.velocity[0] = -self.velocity[0]
      
   def collide_right_paddle(self,paddle):
      paddle_pos = paddle.get_pos() # self.vpos,self.height,self.hpos,self.width
      paddle_left = paddle_pos[2]
      paddle_top = paddle_pos[0]
      paddle_bottom = paddle_pos[0] + paddle_pos[1]
      if self.center[0] + self.radius == paddle_left and paddle_top < self.center[1] < paddle_bottom:
         if self.velocity[0] > 0:
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
   
   def __init__(self, rect_color, velocity, horiz_pos, vert_pos, rect_width, rect_height, surface):
      self.color = rect_color
      self.width = rect_width
      self.height = rect_height
      self.surface = surface
      self.hpos = horiz_pos
      self.vpos = vert_pos
      self.down = False
      self.up = False
      self.velocity = velocity
      self.paddle_position = [self.vpos,self.height,self.hpos,self.width]
         
   def get_pos(self):
      paddle_position = [self.vpos,self.height,self.hpos,self.width]
      return paddle_position
      
   def move_up(self):
      self.up = True
      
   def move_down(self):
      self.down = True
      
   def move_stop(self):
      self.down = False
      self.up = False
         
   def move(self):
      height = self.surface.get_height()
      if self.down and self.vpos + self.height <= height:
         self.vpos = self.vpos + self.velocity
      if self.up and self.vpos >= 0:
         self.vpos = self.vpos - self.velocity
         
   def draw(self):
      pygame.draw.rect(self.surface,self.color,(self.hpos,self.vpos,self.width,self.height))
   
   
main()