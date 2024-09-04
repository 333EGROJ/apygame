import pygame
from player import Player

# Constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Player constants
PLAYER_RADIUS = 20
def main():
    pygame.init()  # Initialize Pygame
    player = Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2, radius=PLAYER_RADIUS) # Initialize the player object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Set up the display
    clock= pygame.time.Clock()
    dt=0
    running = True  # Variable to control the main loop

    while running:
        for event in pygame.event.get():  # Event handling
            if event.type == pygame.QUIT:  # Quit the game if the "close" button is pressed
                running = False
        
        # Update game state here

        screen.fill((0, 0, 0))  # Fill the screen with black color
        player.update(dt)
        # Draw everything here
        player.draw(screen)
        pygame.display.flip()  # Update the display
        dt = clock.tick(60) / 1000

    pygame.quit()  # Clean up and exit Pygame
    
if __name__ == "__main__":
    main()