import pygame
from pygame import *

pygame.init()
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# Charger les images de déplacement des gardiens
Gright_images = [pygame.image.load("ssets/Gardien/anid/cop2idle.png"), pygame.image.load("ssets/Gardien/anid/cop2run1.png"), pygame.image.load("ssets/Gardien/anid/cop2run2.png")]
Gleft_images = [pygame.image.load("ssets/Gardien/anig/cop2idle.png"), pygame.image.load("ssets/Gardien/anig/cop2run1.png"), pygame.image.load("ssets/Gardien/anig/cop2run2.png")]

# Obtenir les dimensions de l'image des gardiens
character_width = Gright_images[0].get_width()
character_height = Gright_images[0].get_height()

# Définir la position initiale du gardien
character_x = window_size[0] // 2
character_y = window_size[1] // 2

# Définir la direction initiale du personnage
direction = 0.5
# pirection = 0.3

# Définir la vitesse de déplacement
move_speed = 0.3

# Compteur de frames pour animer le personnage
frame_counter = 0

# Boucle de jeu principale
running = True
while running:
    
    # Déplacer le personnage en ligne droite
    character_x += 0.5 * direction

    # Faire un aller-retour
    if character_x + character_width >= window_size[0] or character_x <= 0:
        direction = -direction

    # Sélectionner les images du personnage en fonction de la direction
    if direction == 0.5:
        character_images = Gright_images
    else:
        character_images = Gleft_images

    # Sélectionner l'image du personnage en fonction du compteur de frames
    character_image = character_images[frame_counter % 3]

    # Afficher le personnage sur la fenêtre
    screen.blit(character_image, (character_x, character_y))

    # Incrémenter le compteur de frames
    frame_counter += 1

    # Mettre à jour l'affichage
    pygame.display.update()

    # Surveiller les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Quitter Pygame
pygame.quit()


