
import pygame

# Surface, Rect
# Rect(left)

pygame.init()
# Variables
window_resolution = (640, 480)
blue_color = (89, 152, 255)
black_color = (0, 0, 0)
# Nom de la fenêtre
pygame.display.set_caption("Python #36")
# Fenetre et Fond d'écran
window_surface = pygame.display.set_mode(window_resolution)
window_surface.fill(blue_color)

## Tracer une ligne
pygame.draw.line(window_surface, black_color, [100, 100], [20,20])

## Tracer un rectangle rempli de noir
# info dans la variable
rectangle1 = pygame.Rect(10, 10, 150, 65)
# Tracer du rectangle
pygame.draw.rect(window_surface, black_color, rectangle1)

## Tracer un rectangle vide épaisseur = 5
# info dans la variable
rectangle2 = pygame.Rect(200, 10, 150, 65)
# Tracer du rectangle
pygame.draw.rect(window_surface, black_color, rectangle2, 5)

## Tracer un Cercle
pygame.draw.circle(window_surface, black_color, [150, 250], 50)

## Tracer un Polygone
polygon1 = [(300, 300), (350, 310), (330, 350)]
pygame.draw.polygon(window_surface, black_color, polygon1, 2)

# Rafraichissement de l'affichage
pygame.display.flip()

# Boucle
launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
