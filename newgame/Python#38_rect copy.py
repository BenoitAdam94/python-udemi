
import pygame
import time

"""
rectangle2 = Rect.copy() # faire une copie
Rect.move
Rect.move_ip()
Rect.inflate() # agrandir/reduire le rectangle

Rect.colliderect() # collision

pygame(x, y, width, height)
"""

pygame.init()
window_resolution = (640, 480)
red = (255, 0, 0)
black = (255, 255, 255)
blue = (0, 0, 255)
i = 0

pygame.display.set_caption("Python #38")
window_surface = pygame.display.set_mode(window_resolution)

# rectangle dans variable
myrect = pygame.Rect(10, 100, 25, 25)
mybloc = pygame.Rect(600, 50, 20, 300)
# dessiner le rectange
"""
pygame.draw.rect(window_surface, red, myrect)
pygame.draw.rect(window_surface, black, mybloc)
pygame.display.flip()
"""


"""
while i < 10:
    time.sleep(0.05)
    window_surface.fill(black)
    myrect.x += 10
    myrect.y += 10
    pygame.draw.rect(window_surface, red, myrect)
    pygame.display.flip()
    i += 1
"""

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
            
    while not myrect.colliderect(mybloc):
        time.sleep(.010)
        window_surface.fill(black)
        myrect.x += 1
        pygame.draw.rect(window_surface, red, myrect)
        pygame.draw.rect(window_surface, blue, mybloc)
        pygame.display.flip()