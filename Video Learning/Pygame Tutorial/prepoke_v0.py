# Pre-Poke The Dots Version Zero
# we are learning how to do the following things:
#
# learn how to open a graphical window
# learn how to keep the graphical window open until the Close button is pressed
# set title window
# draw basic geometic shapes
#   draw a circle 
#   draw a rectangle
# change the color of geometic shapes
# respond to user input (close window)
import pygame, sys


def main():

    #initialize pygame -- required for rendering fonts
    pygame.init()
    
    # creat the window and set its size to 500 width and 400 height
    size = (500,400)
    screen = pygame.display.set_mode(size)
    
    # set the title of the window
    pygame.display.set_caption("Poke The Dots Preperation v0")
    
    # enter our main gameplay loop, repeating until the user clicks the windows close button
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        # draw a green circle with radius 100 at position 150, 150 on screen
        circle_color = pygame.Color('green')
        circle_pos = (150, 150)
        circle_radius = 100
        pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)
        
        # draw a blue rectangle with height 50 and width 200 at position 0,0 on screen
        rect_color = pygame.Color('blue')
        rect_left = 0
        rect_top = 0
        rect_width = 200
        rect_height = 50
        rect_params = pygame.Rect(rect_left,rect_top,rect_width,rect_height)
        pygame.draw.rect(screen, rect_color, rect_params)
    
        # render all drawn objects to the screen
        pygame.display.flip()

main()