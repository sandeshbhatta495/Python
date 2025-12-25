import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Line Scaling Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Function to draw a line and its scaled version
def draw_line(x1, y1, x2, y2, scale_x, scale_y):
    # Original line
    pygame.draw.line(screen, RED, (x1, y1), (x2, y2), 3)
    
    # Scaled line
    scaled_x1 = int(x1 * scale_x)
    scaled_y1 = int(y1 * scale_y)
    scaled_x2 = int(x2 * scale_x)
    scaled_y2 = int(y2 * scale_y)
    
    pygame.draw.line(screen, BLUE, (scaled_x1, scaled_y1), (scaled_x2, scaled_y2), 3)
    
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
        # Apply scaling factors (scale_x, scale_y) = (1.5, 1.5)
        draw_line(100, 100, 500, 400, 1.5, 1.5)

        # Update the display
        pygame.display.flip()

# Run the program
if __name__ == "__main__":
    main()
