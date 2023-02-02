import pygame
from pygame import *

pygame.init()
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# Charger la map
# background_image = pygame.image.load("ssets/map/map1.bmp")

# Charger les images du personnage principal
# Pright_images = [pygame.image.load("ssets/persop/anid/playeridle.png"), pygame.image.load("ssets/persop/anid/playerrun1.png"), pygame.image.load("ssets/persop/anid/playerrun2.png")]
# Pleft_images = [pygame.image.load("ssets/persop/anig/playeridle.png"), pygame.image.load("ssets/persop/anig/playerrun1.png"), pygame.image.load("ssets/persop/anig/playerrun2.png")]
# Pstand_image = [pygame.image.load("ssets/persop/anid/playeridle.png"),pygame.image.load("ssets/persop/anid/playeridle.png"),pygame.image.load("ssets/persop/anid/playeridle.png")]
# Pstang_image = [pygame.image.load("ssets/persop/anig/playeridle.png"),pygame.image.load("ssets/persop/anig/playeridle.png"),pygame.image.load("ssets/persop/anig/playeridle.png")]

# Charger les images de déplacement des gardiens
Gright_images = [pygame.image.load("ssets/Gardien/anid/cop2idle.png"), pygame.image.load("ssets/Gardien/anid/cop2run1.png"), pygame.image.load("ssets/Gardien/anid/cop2run2.png")]
Gleft_images = [pygame.image.load("ssets/Gardien/anig/cop2idle.png"), pygame.image.load("ssets/Gardien/anig/cop2run1.png"), pygame.image.load("ssets/Gardien/anig/cop2run2.png")]

# Obtenir les dimension du perso
# pharacter_width = Pright_images[0].get_width()
# pharacter_height = Pright_images[0].get_height()

# Obtenir les dimensions de l'image des gardiens
character_width = Gright_images[0].get_width()
character_height = Gright_images[0].get_height()

# Définir la position initiale du personnage
# pharacter_x = window_size[0] // 35
# pharacter_y = window_size[1] // 15

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
    # Afficher l'image de fond sur la fenêtre
    # screen.blit(background_image, (0, 0))

    # Déplacer le personnage en ligne droite
    character_x += 0.5 * direction

    # keys = pygame.key.get_pressed()
    # # Déplacer le personnage en fonction de la touche appuyée
    # if keys[pygame.K_UP] and pharacter_y > 13:
    #     pharacter_y -= move_speed
    # if keys[pygame.K_DOWN] and pharacter_y < 430:
    #     pharacter_y += move_speed
    # if keys[pygame.K_LEFT] and pharacter_x > 15:
    #     pharacter_x -= move_speed
    #     pharacter_images = Pleft_images
    # else: pharacter_images = Pstang_image
    # if keys[pygame.K_RIGHT] and pharacter_x < 766:
    #     pharacter_x += move_speed
    #     pharacter_images = Pright_images
    # else: pharacter_images = Pstand_image

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
    # pharacter_image = pharacter_images[frame_counter % 3]

    # Afficher le personnage sur la fenêtre
    screen.blit(character_image, (character_x, character_y))
    # screen.blit(pharacter_image, (pharacter_x, pharacter_y))

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


