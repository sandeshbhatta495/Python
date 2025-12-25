import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Line Translation Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Function to draw a line and its translated version
def draw_line(x1, y1, x2, y2, tx, ty):
    # Original line
    pygame.draw.line(screen, RED, (x1, y1), (x2, y2), 3)
    
    # Translated line
    translated_x1 = x1 + tx
    translated_y1 = y1 + ty
    translated_x2 = x2 + tx
    translated_y2 = y2 + ty
    
    pygame.draw.line(screen, GREEN, (translated_x1, translated_y1), (translated_x2, translated_y2), 3)
    
    pygame.display.flip()

# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # Original line from (100, 100) to (500, 400)
        # Apply translation (tx, ty) = (150, 100)
        draw_line(100, 100, 500, 400, 150, 100)

        # Update the display
        pygame.display.flip()

# Run the program
if __name__ == "__main__":
    main()
