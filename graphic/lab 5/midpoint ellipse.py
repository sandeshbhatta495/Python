import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint Ellipse  Drawing Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED= (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
BRICK = (178, 34, 34)
PINK = (255, 192, 203)
ORANGE = (255, 165, 0)
BROWN = (165, 42, 42)

#Rainbow colors
rainbow = [RED, ORANGE, YELLOW, GREEN, BLUE, PINK, BRICK]

# Function to draw a circle using the midpoint ellipse algorithm
def draw_ellipse (xc, yc, rx,ry):
    x = 0
    y = ry
    p = ry**2-rx**2*ry+(1/4)*rx**2

    # Draw the initial points
    def plot_points(xc, yc, x, y):
        screen.set_at((xc + x, yc + y), WHITE)
        screen.set_at((xc - x, yc + y), RED)
        screen.set_at((xc + x, yc - y), GREEN)#first 
        screen.set_at((xc - x, yc - y), YELLOW)
        screen.set_at((xc + y, yc + x), BLUE)
        screen.set_at((xc - y, yc + x), BRICK)
        screen.set_at((xc + y, yc - x), PINK)
        screen.set_at((xc - y, yc - x), ORANGE)
        pygame.time.delay(20)
        pygame.display.flip()

    plot_points(xc, yc, rx, ry)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * x - 2 * y + 1
        plot_points(xc, yc, x, y)

# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(WHITE)

        # Draw circle using the midpoint circle algorithm
        draw_ellipse(400, 100, 100)  
        draw_ellipse(400, 300, 100) 
        draw_ellipse(400, 500, 100)
        draw_ellipse(200, 300, 100)
        draw_ellipse(600, 300, 100)  
        pygame.draw.ellipse (screen, BROWN, (400, 300), 100, 100)
        pygame.draw.ellipse (screen, BROWN, (400, 300), 100, 10)
        pygame.draw.ellipse (screen, BROWN, (400, 300), 100, 1)
        pygame.draw.ellipse (screen, BROWN, (400, 300), 100, 50)
        pygame.draw.ellipse (screen, BROWN, (400, 300), 100, 25)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
