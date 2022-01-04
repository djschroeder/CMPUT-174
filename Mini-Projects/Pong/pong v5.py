# Pong Game
# players use a paddle to prevent the ball from hitting their side of the screen
# if ball collides with opposing side of screen that player gets a point
# game ends when one player reaches a score of 11

import pygame

def main():
   # creates a game object
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
      # Game objects creation
      self.ball = Ball('white', 5, [400, 50], [-6,1], self.surface)
      self.paddle_left = Paddle('white',3,75,180,10,40,self.surface)
      self.paddle_right = Paddle('white',3,425,180,10,40,self.surface)
      self.score_left = 0
      self.score_right = 0

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
      events = pygame.event.get() # moves all game events into events variable
      for event in events: 
         # iterates through each event in events
         if event.type == pygame.QUIT:
            self.close_clicked = True
         if event.type == pygame.KEYDOWN:
            # checks if a paddle control key has been pressed and calls the coorisponding paddle move function
            if event.key == pygame.K_q:
               self.paddle_left.move_up()
            if event.key == pygame.K_a:
               self.paddle_left.move_down()
            if event.key == pygame.K_p:
               self.paddle_right.move_up()
            if event.key == pygame.K_l:
               self.paddle_right.move_down()            
         if event.type == pygame.KEYUP:
            # stops paddle movement by calling paddle stop function if a control key is released
            if event.key == pygame.K_q or event.key == pygame.K_a:
               self.paddle_left.move_stop()
            if event.key == pygame.K_p or event.key == pygame.K_l:
               self.paddle_right.move_stop()
        
   def draw(self):
      # Draws all game objects.
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
      self.score()
      
   def draw_score(self,side,score):
      # Draws scores in top corners
      # - self is the Game 
      # - side is type str and determines what corner score should be drawn in
      # - score is type int and is the current score of the player
      score_string = str(score)
      font_size = 80
      fg_color = pygame.Color('white')
      font = pygame.font.SysFont('Times New Roman', font_size)
      text_box = font.render(score_string, True, fg_color, self.bg_color)
      # following if statement determines where to draw the score
      if side == 'left':
         location = (0,0)
      elif side == 'right':
         location = (self.surface.get_width()-text_box.get_width(),0)
      self.surface.blit(text_box,location)   
      
   def score(self):
      # Determines if a player scored a point and updates score
      # - self is the Game whose score is updated
      if self.ball.get_center()[0] - self.ball.get_radius() < 1:
         self.score_right = self.score_right + 1
      if self.ball.get_center()[0] + self.ball.get_radius() > self.surface.get_width()-1:
         self.score_left = self.score_left + 1     
         
   def decide_continue(self):
      # Determines if game should contine
      # - self is the Game to decide whether it should continue
      winning_score = 11
      if self.score_left == winning_score or self.score_right == winning_score:
         self.continue_game = False

class Ball:
   # An object in this class represents a moving ball
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
      
   def get_radius(self):
      # Getter method returns ball radius
      # - self is the Ball whose radius is being reqested
      return self.radius
   
   def get_center(self):
      # Getter method returns ball center
      # - self is the Ball whose center is being requested
      return self.center
   
   def collide_left_paddle(self,paddle):
      # Determines if ball collides with left paddle
      # - self is the ball that is colliding
      # - paddle is type Paddle and is the left player paddle the ball is colliding into
      paddle_pos = paddle.get_pos() # list containing paddle position in the form of [vpos,height,hpos,width]
      paddle_right = paddle_pos[2] + paddle_pos[3]
      paddle_left = paddle_pos[2]
      paddle_top = paddle_pos[0]
      paddle_bottom = paddle_pos[0] + paddle_pos[1]
      if (paddle_left < self.center[0] - self.radius < paddle_right) and (paddle_top < self.center[1] < paddle_bottom):
         if self.velocity[0] < 0:
            self.velocity[0] = -self.velocity[0]
      
   def collide_right_paddle(self,paddle):
      # Determines if ball collides with right paddle
      # - self is the ball that is colliding
      # - paddle is type Paddle and is the right player paddle the ball is colliding into    
      paddle_pos = paddle.get_pos() # list containing paddle position in the form of [vpos,height,hpos,width]
      paddle_right = paddle_pos[2] + paddle_pos[3]
      paddle_left = paddle_pos[2]
      paddle_top = paddle_pos[0]
      paddle_bottom = paddle_pos[0] + paddle_pos[1]
      if paddle_right > self.center[0] + self.radius > paddle_left and paddle_top < self.center[1] < paddle_bottom:
         if self.velocity[0] > 0:
            self.velocity[0] = -self.velocity[0]      
      
   def move(self):
      # Changes the location of the ball by adding the corresponding 
      # speed values to the x and y coordinate of its center
      # - self is the ball that is moving
      size = self.surface.get_size()
      for i in range(0,2):
         self.center[i] = (self.center[i] + self.velocity[i])
         if self.center[i] < self.radius: # left or top edge
            self.velocity[i] = -self.velocity[i]
         if self.center[i] + self.radius > size[i]:
            self.velocity[i] = -self.velocity[i]
      
   def draw(self):
      # Draws the ball on the surface
      # - self is the ball
      pygame.draw.circle(self.surface, self.color, self.center, self.radius)

class Paddle:
   # An object in this class represents a player paddle
   def __init__(self, rect_color, velocity, horiz_pos, vert_pos, rect_width, rect_height, surface):
      # Initialize a paddle
      # - self is the paddle to initialize
      # - rect_color is type str gives the color of the paddle
      # - velocity is type int and determines how fast the paddle can move
      # - horiz_pos is type int and determines horizontal starting position
      # - vert_pos is type int and determines vertical starting position
      # - rect_width is type int and determines paddle width
      # - rect_height is type int and determines paddle height
      # - surface is the the windows pygame.Surface object
      self.color = pygame.Color(rect_color)
      self.velocity = velocity
      self.hpos = horiz_pos
      self.vpos = vert_pos
      self.width = rect_width
      self.height = rect_height      
      self.surface = surface
      self.down = False
      self.up = False
      
   def get_pos(self):
      # collects and returns Paddle position data 
      # - self is the Paddle whose position is being requested
      paddle_position = [self.vpos,self.height,self.hpos,self.width]
      return paddle_position
      
   def move_up(self):
      # starts paddle up movement
      # - self is the Paddle that is being moved up
      self.up = True
      
   def move_down(self):
      # starts paddle down movement
      # - self is the Paddle that is being moved down      
      self.down = True
      
   def move_stop(self):
      # Stops all paddle movement
      # - self is the Paddle that is stopped
      self.down = False
      self.up = False
         
   def move(self):
      # Determines new paddle position
      # - self is the Paddle that is being moved
      height = self.surface.get_height()
      if self.down and self.vpos + self.height <= height:
         self.vpos = self.vpos + self.velocity
      if self.up and self.vpos >= 0:
         self.vpos = self.vpos - self.velocity
      
   def draw(self):
      # Draws the Paddle to the game surface
      # - self is the Paddle that is being drawn
      pygame.draw.rect(self.surface,self.color,(self.hpos,self.vpos,self.width,self.height))
   
main()