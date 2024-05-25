import pygame
from config import *
pygame.init()

game_in_play = True
score = 0
lives = 5

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

while game_in_play:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_in_play = False
    
    clock.tick(60)

    screen.fill(BLACK)

    pygame.display.flip()