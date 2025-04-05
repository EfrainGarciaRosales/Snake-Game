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