import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BLA Line Drawing Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to draw a line using DDA algorithm
def draw_line_breseb(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if x2>x1:
        lx=1
    else:
        lx=-1

    if y2>y1:
        ly=1
    else:
        ly=-1

    x=x1
    y=y1
    if dx>dy:
        for i in range(x1,x2):
            p=(2*dy)-dx
            if p<0:
                x=x+lx
                y=yp=p+(2*dy)
            else:
                x=x+lx
                y=y+ly
                p=p+(2*dy)-(2*dx)
    else:
        for i in range(y1,y2):
            p=(2*dx)-dy
            if p<0:
                x=x
                y=y+ly
                p=p+(2*dx)
            else:
                x=x+lx
                y=y+ly
                p=p+(2*dx)-(2*dy)
                screen.set_at((round(x), round(y)), WHITE)
   


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
        draw_line_breseb(100,100 , 300, 300)
       


        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()