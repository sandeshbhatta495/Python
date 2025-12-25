import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Line Rotation Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Function to rotate a point around the origin (0, 0)
def rotate_point(x, y, angle):
    angle_rad = math.radians(angle)  # Convert angle to radians
    x_new = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    y_new = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    return int(x_new), int(y_new)

# Function to draw a line and its rotated version
def draw_line(x1, y1, x2, y2, angle):
    # Original line
    pygame.draw.line(screen, RED, (x1, y1), (x2, y2), 3)
    
    # Rotate the endpoints of the line
    x1_rot, y1_rot = rotate_point(x1, y1, angle)
    x2_rot, y2_rot = rotate_point(x2, y2, angle)
    
    # Rotated line
    pygame.draw.line(screen, YELLOW, (x1_rot, y1_rot), (x2_rot, y2_rot), 3)
    
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
        # Apply rotation angle of 45 degrees
        draw_line(100, 100, 500, 400, 45)

        # Update the display
        pygame.display.flip()

# Run the program
if __name__ == "__main__":
    main()
