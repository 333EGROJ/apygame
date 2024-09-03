import pygame

# Constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():
    pygame.init()  # Initialize Pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Set up the display

    running = True  # Variable to control the main loop

    while running:
        for event in pygame.event.get():  # Event handling
            if event.type == pygame.QUIT:  # Quit the game if the "close" button is pressed
                running = False
        
        # Update game state here

        screen.fill((0, 0, 0))  # Fill the screen with black color

        # Draw everything here

        pygame.display.flip()  # Update the display

    pygame.quit()  # Clean up and exit Pygame

if __name__ == "__main__":
    main()