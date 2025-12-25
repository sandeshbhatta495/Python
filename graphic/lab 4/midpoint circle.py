import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mid point Drawing Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# function to draw  circle using midpoint circle algorithm
def draw_circle(xc,yc,r):
    xc=0
    yc=r
    p0=1-r
    if p0<0:
        x=xc+1
        y=yc
        p=p0+2*x+1
    else:
        x=xc+1
        y=yc-1
        p=p0+2*x-2*y+1

    while x<y:
        screen.set_at((x+xc,y+yc),WHITE)
        screen.set_at((-x+xc,y+yc),WHITE)
        screen.set_at((x+xc,-y+yc),WHITE)
        screen.set_at((-x+xc,-y+yc),WHITE)
        screen.set_at((y+xc,x+yc),WHITE)
        screen.set_at((-y+xc,x+yc),WHITE)
        screen.set_at((y+xc,-x+yc),WHITE)
        screen.set_at((-y+xc,-x+yc),WHITE)
        if p<0:
            x=x+1
            p=p+2*x+1
        else:
            x=x+1
            y=y-1
            p=p+2*x-2*y+1
# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # Draw circle usng midpoint circle algorithm
        draw_circle(100,100,10)

        
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()