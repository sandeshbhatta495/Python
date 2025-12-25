import pygame
import sys
import math
import datetime

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mechanical Clock")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
SILVER = (192, 192, 192)
GREEN = (34, 139, 34)
BLUE = (70, 130, 180)
RED = (255, 0, 0)
BORDER_COLOR = (255, 165, 0)
DAY_BOX_COLOR = (0, 0, 128)
TEXT_COLOR = (255, 255, 255)

font = pygame.font.Font(None, 40)

background = pygame.image.load(r"C:\Users\DELL\Pictures\Screenshots\bg.png")
bg_width, bg_height = background.get_width(), background.get_height()
scale_factor = min(WIDTH / bg_width, HEIGHT / bg_height)
new_bg_width = int(bg_width * scale_factor)
new_bg_height = int(bg_height * scale_factor)
background = pygame.transform.scale(background, (new_bg_width, new_bg_height))
bg_x = (WIDTH - new_bg_width) // 2
bg_y = (HEIGHT - new_bg_height) // 2

def rotate_point(cx, cy, length, angle_deg):
    angle_rad = math.radians(angle_deg - 90)
    x = cx + length * math.cos(angle_rad)
    y = cy + length * math.sin(angle_rad)
    return int(x), int(y)

def draw_hand(cx, cy, length, angle, color, thickness):
    x_end, y_end = rotate_point(cx, cy, length, angle)
    pygame.draw.line(screen, color, (cx, cy), (x_end, y_end), thickness)

def draw_numbers(cx, cy, radius):
    for i in range(12):
        angle = 30 * i
        x, y = rotate_point(cx, cy, radius - 40, angle)
        number_text = font.render(str(i if i != 0 else 12), True, WHITE)
        text_rect = number_text.get_rect(center=(x, y))
        screen.blit(number_text, text_rect)

def draw_day_and_symbol():
    day = datetime.datetime.now().strftime('%a')
    symbol = get_day_symbol(day)
    
    day_box_rect = pygame.Rect(WIDTH - 200, HEIGHT // 2 - 50, 180, 60)
    pygame.draw.rect(screen, DAY_BOX_COLOR, day_box_rect)
    pygame.draw.rect(screen, WHITE, day_box_rect, 3)

    day_text = font.render(day, True, TEXT_COLOR)
    screen.blit(day_text, (WIDTH - 180, HEIGHT // 2 - 40))

    symbol_text = font.render(symbol, True, TEXT_COLOR)
    screen.blit(symbol_text, (WIDTH - 180, HEIGHT // 2 + 5))

def get_day_symbol(day):
    symbols = {
        'Sun': '☀️',
        'Mon': '🌙',
        'Tue': '🌞',
        'Wed': '🌛',
        'Thu': '🌝',
        'Fri': '🌜',
        'Sat': '🌕',
    }
    return symbols.get(day, '')

def draw_clock():
    cx, cy = WIDTH // 2, HEIGHT // 2
    radius = 200

    now = datetime.datetime.now()
    hour, minute, second = now.hour % 12, now.minute, now.second

    second_angle = second * 6
    minute_angle = minute * 6 + second * 0.1
    hour_angle = hour * 30 + minute * 0.5

    screen.fill(BLACK)
    screen.blit(background, (bg_x, bg_y))

    pygame.draw.rect(screen, BORDER_COLOR, (10, 10, WIDTH - 20, HEIGHT - 20), 5)
    pygame.draw.rect(screen, WHITE, (15, 15, WIDTH - 30, HEIGHT - 30), 3)

    pygame.draw.circle(screen, SILVER, (cx, cy), radius, 3)
    draw_numbers(cx, cy, radius)
    draw_hand(cx, cy, 90, hour_angle, GREEN, 6)
    draw_hand(cx, cy, 130, minute_angle, BLUE, 4)
    draw_hand(cx, cy, 170, second_angle, RED, 2)
    draw_day_and_symbol()

def main():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_clock()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()