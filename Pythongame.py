import pygame

pygame.init()

width = 640
height = 480

screen = pygame.display.set_mode((width, height))
texture = pygame.image.load("enemy.png")

posX = 0
posY = 0

velX = 1
velY = 0.5

gameover = False

while not gameover:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            gameover = True
        
        posX += velX
        posY += velY
        
        screen.fill ((0, 0 , 0))
        screen.blit(texture, (posX, posY))
        pygame.display.flip()