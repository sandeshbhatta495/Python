import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DDA Line Drawing Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to draw a line using DDA algorithm
def draw_line_dda(x1, y1, x2, y2):
    
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    if dx>dy:
        step=dx
    else:
        step=dy

    xinc=dx/step
    yinc=dy/step
    x=x1
    y=y1
    for i in range(1,step):
        x=x+xinc
        y=y+yinc
        screen.set_at((round(x),round(y)),WHITE)
    
    

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
        draw_line_dda(100, 100, 400,400)#right hand to left cross line 
        draw_line_dda(100, 100, 100,400)#horizontal line from left 
        draw_line_dda(400, 100, 400,400)#horizontal line from right
       



        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
