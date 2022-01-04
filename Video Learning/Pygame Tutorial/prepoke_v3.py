# Pre-Poke The Dots Version Zero

# Working on splitting up what we've learned into code segments that are specific to poke the dots
# and code segments that will be general to all games we talk about

import pygame, sys

def main():
    #initialize pygame -- required for rendering fonts
    pygame.init()
    
    # creat the window and set its size to 500 width and 400 height
    size = (500,400)
    screen = pygame.display.set_mode(size)
    
    # set the title of the window
    pygame.display.set_caption("Poke The Dots Preperation v0")
    
    # game objects and variables that are general to games
    bg_color = pygame.Color('black')
    game_clock = pygame.time.Clock()
    FPS = 30
    continue_game = True
    
    # game objects that are specific to poke the dots
    circle_color = pygame.Color('green')
    circle_pos = [150, 150]
    circle_velocity = [1,1]
    circle_radius = 30  
    frame_counter = 0
    max_frames = 100    
    
    # ==Main Gameplay Loop
    # Each iteration over the loop will draw the dot at a static location
    # We will then move the dot a small amount, redraw the dot, and repeats
    # many times a second to give the appearance of motion.
    #
    # This will repeat until the user clics the windows 'close' button
    # 
    # handle user input (event handling)
    # draw game objects
    # check for game over conditions
    # if the game over conditions are not yet met:
    #     then update the game state
    #     (including checking for game over conditions)
    while True:
        # event handling
        #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()  # pygame.exit() is not valid
                
        # draw game objects
        #
        # clear out screen before we draw game object
        screen.fill(bg_color)
        # draw aour dot to screenand then move its location 
        # for next time to create the illusion of motion
        pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)
        # render all drawn objects to the screen
        pygame.display.flip()
        
        # look at game over conditions
        # if those conditions are not met:
        #     update the game state
        #     check if game over conditions are now met
        if continue_game:
            
            # update game objects (in this game, move our circle to a new location)
            for index in range(0,2):
                circle_pos[index] = circle_pos[index] + circle_velocity[index]
            frame_counter = frame_counter + 1
            
            # check if game over conditions are met
            if frame_counter > max_frames:
                continue_game = False
            
        game_clock.tick(FPS)
        
main()