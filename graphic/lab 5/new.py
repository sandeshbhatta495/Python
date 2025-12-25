import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DDA Line Drawing Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Function to draw a line
def translation(x1, y1, x2, y2, tx, ty):
    pygame.draw.line(screen, RED, (x1, y1), (x2,y2), 5)
    x11 = x1 + tx
    x22 = x2 + tx
    y11 = y1 + ty
    y22 = y2 + ty
    pygame.draw.line(screen, YELLOW, (x11, y11), (x22, y22), 5)

def rotation(x1, y1, x2, y2, angle):
    pygame.draw.line(screen, RED, (x1, y1), (x2, y2), 4)
    rad = math.radians(angle)
    xr = x2 * math.cos(rad) - y2 * math.sin(rad)
    yr = x2* math.sin(rad) + y2 * math.cos(rad)

    pygame.draw.line(screen, GREEN, (x1, y1), (xr, yr), 4)

def scaling(x1, y1, x2, y2, sx, sy):
    x22 = x2 * sx
    y22 = y2 * sy
    pygame.draw.line(screen, BLUE, (x1, y1), (x22, y22))


# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # Draw a line using DDA algorithm
        translation(200, 100, 400, 200, 200, 200)
        rotation(200, 100, 400, 200, 45)
        scaling(200, 100, 400, 200, 2, 2)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()