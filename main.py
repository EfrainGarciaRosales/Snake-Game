import pygame
import random


# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake and food block size
block_size = 20
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], block_size, block_size])

def message(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, [width / 6, height / 3])

def game_loop():
    game_over = False
    game_close = False

    x = width // 2
    y = height // 2
    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(white)
            message("You Lost! Press Q to Quit or C to PLay Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_q:
                        game_over = True
                        game_close = False
                if event.keyu == pygame.K_c:
                    game_loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -block_size
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = -block_size
                        y_change = 0
                    elif event.key == pygame.K_UP:
                        y_change = -block_size
                        x_change = 0
                    elif event.key == pygame.K_DOWN:
                        y_change = block_size
                        x_change = 0
            x += x_change
            y += y_change

            if x >= width or x < 0 or y >= height or y < 0:
                game_close = True

            screen.fill(white)
            pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])

            snake_head = []
            snake_head.append(x)
            snake_head.append(y)
            snake_list.append(snake_head)

            if len(snake_list) > length_of_snake:
                del snake_list[0]

            for segment in snake_list[:-1]:
                if segment == snake_head:
                    game_close = True

            draw_snake(snake_list)
            pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - block_size) /20.0) * 20.0
            length_of_snake += 1

        clock.tick(10)

    pygame.quit()
    quit()

game_loop()
