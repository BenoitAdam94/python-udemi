
import pygame

pygame.init()
window_resolution = (640, 480)

pygame.display.set_caption("Python #38")
window_surface = pygame.display.set_mode(window_resolution)

blue = (0, 75, 255)
white = (255, 255, 255)


# roboto = pygame.font.Font("Roboto.tff", 32) # font dans le dossier
arial_font = pygame.font.SysFont("arial", 30, True, False) # font taille gras italique
hello_text = arial_font.render("Hello é^$€*à !", False, blue, white) # anti-aliasing / couleur / fond

window_surface.blit(hello_text, [10, 10])
pygame.display.flip()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False


print(pygame.font.get_fonts()) # liste polices installée sur le PC