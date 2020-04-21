
import pygame

pygame.init()
window_resolution = (640, 480)
blank_color = (255, 255, 255)

pygame.display.set_caption("Python #37")
window_surface = pygame.display.set_mode(window_resolution)
#chargement de l'image
image1 = pygame.image.load("ball.png")

# convertir format de l'image (optimisation)
image1.convert()

# Boucle
launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    ## Corps du programme
    
    # Point en haut à gauche
    window_surface.fill(blank_color)
    window_surface.blit(image1, [10, 10])
    pygame.display.flip()