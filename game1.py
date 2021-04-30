import pygame
from car import Car
pygame.init()

#colour def
BLK = (0, 0, 0)
WHT = (255, 255, 255)
GRN = (0, 255, 0)
RED = (255, 0, 0)
BLU = (0, 0, 255)
GRY = (210, 210 ,210)

#open window
size = (400, 300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hello World! (game1)")

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#list containing all sprites
all_sprites_list = pygame.sprite.Group()

#car init
playerCar1 = Car(RED, 20, 50)
playerCar1.rect.x = 250
playerCar1.rect.y = 200
all_sprites_list.add(playerCar1)

playerCar2 = Car(BLU, 20, 30)
playerCar2.rect.x = 100
playerCar2.rect.y = 150
all_sprites_list.add(playerCar2)

# -------- Main Program Loop -----------
while carryOn: 
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            carryOn = False # Flag that we are done so we exit this loop

    # --- Game logic should go here
    all_sprites_list.update()

    # First, clear the screen to white.
    screen.fill(WHT)

    # --- Drawing road              X_pos, y_pos, width, depth
    pygame.draw.rect(screen, GRY, [50, 0, 300, 300],0)
    pygame.draw.line(screen, WHT, [200, 0],[200, 300], 5)
    #                             X,y pos start, x,y pos finish, line width
    # --- drawing sprites
    all_sprites_list.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
