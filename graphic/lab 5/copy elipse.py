import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ellipse Drawing Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to draw a  ellipse  algorithm
def draw_ellipse(rx, ry, xc, yc):
        x = 0
        y = ry
        rx2 = rx**2
        ry2 = ry**2

        # Region 1
        p1 = (ry2) - (rx2*ry) + (rx2)/4

        def plot_points(xc, yc, x, y):
        # Plot the symmetrical points for all quadrants
             screen.set_at((xc + x, yc + y), "BLUE")
             screen.set_at((xc - x, yc + y), "BLUE")
             screen.set_at((xc + x, yc - y), "BLUE")
             screen.set_at((xc - x, yc - y), "BLUE")
             screen.set_at((xc + y, yc + x), "BLUE")
             screen.set_at((xc - y, yc + x), "WHITE")
             screen.set_at((xc + y, yc - x), "PINK")
             screen.set_at((xc - y, yc - x), "ORANGE")
             
             pygame.time.delay(20)
             pygame.display.flip()




        while (2* ry2 * x) <= (2 * rx2 * y):
             x += 1
             if p1 < 0:
                  y = y
                  p1 += 2* ry2 *x + ry2
            
             else:
                y = y - 1
                p1 += 2*ry2*x - 2*rx2*y + ry2  
             plot_points(xc, yc, x, y)    
        
    
        # Region 2
        p2 = ry2 * (x + 0.5)**2 + rx2 * (y - 1)**2 - rx2 * ry2
        while y > 0:
             y -= 1
             if p2 > 0:
                p2 -= 2*rx2 * y + rx2
             else:
                x += 1
                p2 += 2*ry2 * x - 2*rx2 * y + rx2
             plot_points(xc, yc, x, y)
        
# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # Draw an ellipse
        draw_ellipse(70, 100, 500, 300)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()