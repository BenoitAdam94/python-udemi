
import pygame

blank_color = (255, 255, 255)
blue_color = (0, 0, 255)
black_color = (0, 0, 0)

pygame.init()
window_resolution = (640, 480)


pygame.display.set_caption("Python #37")
window_surface = pygame.display.set_mode(window_resolution)
#chargement de l'image
image1 = pygame.image.load("ball.png")

# convertir format de l'image (optimisation)
image1.convert()

# PNG avec transparence
image2 = pygame.image.load("heart.png")
image2.convert_alpha() # ne semble pas obligatoire mais good practice

# JPG avec transparence
image3 = pygame.image.load("ball.jpg")
image3.set_colorkey(blank_color)

# Boucle
launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    ## Corps du programme
    
    
    
    window_surface.fill(blue_color)
    # Affichage de l'image = Point en haut à gauche de l'image comme point de reference
    window_surface.blit(image1, [10, 10]) 
    window_surface.blit(image2, [100, 100])
    window_surface.blit(image3, [200, 200])
    pygame.display.flip()