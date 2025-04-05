import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# colors
white = (255, 255, 255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake and food block size
block_size = 20
clock = pygame.time.Clock()
font = pygame.font.SysFont(none, 35)

def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen,green,[block[0],block[1],block_size, block_size])

def message(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, [width / 6, height / 3])

def game_loop ():
    game_over = False
    game_close = False
    x = width //2
    y = height //2
    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1
