import pygame

pygame.init()
ttt = pygame.display.set_mode((300, 325))
pygame.display.set_caption('Tic-Tac-Toe')

running = True

while (running):
    for event in pygame.event.get():
        if event.type is QUIT:
            running = 0