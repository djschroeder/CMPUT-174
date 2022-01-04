# Pre-Poke The Dots Version Zero

import pygame, sys


def main():
    #initialize pygame -- required for rendering fonts
    pygame.init()
    
    # creat the window and set its size to 500 width and 400 height
    size = (500,400)
    screen = pygame.display.set_mode(size)
    
    # set the title of the window
    pygame.display.set_caption("Poke The Dots Preperation v0")
    
    # initialize game objects
    bg_color = pygame.Color('black')
    
    game_clock = pygame.time.Clock()
    FPS = 30
    
    circle_color = pygame.Color('green')
    circle_pos = [150, 150]
    circle_velocity = [1,1]
    circle_radius = 30    
    
    # ==Main Animation Loop
    # Each iteration over the loop will draw the dot at a static location
    # We will then move the dot a small amount, redraw the dot, and repeats
    # many times a second to give the appearance of motion.
    #
    # This will repeat until the user clics the windows 'close' button
    # enter our main gameplay loop, repeating until the user clicks the windows close button
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()  # pygame.exit() is not valid
    
        # clear out screen before we draw game object
        screen.fill(bg_color)
        
        # draw aour dot to screenand then move its location 
        # for next time to create the illusion of motion
        pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)
        for index in range(0,2):
            circle_pos[index] = circle_pos[index] + circle_velocity[index]
        
        # render all drawn objects to the screen
        pygame.display.flip()
        game_clock.tick(FPS)
        
main()