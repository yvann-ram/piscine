import pygame
from pygame import *
# classes
from classes.Personnage import Personnage
from classes.Inventaire import Inventaire
from classes.Objet import Objet

pygame.init()

# CREATING CANVAS
screen = pygame.display.set_mode((800, 800))
inventaire = Inventaire()
cle_porte = Objet("clé de la porte", 1)
cle_coffre = Objet("clé du coffre", 1)
personnage = Personnage(inventaire, (400, 400))
inventaire.Add(cle_porte)
inventaire.Add(cle_coffre)
inventaire.Remove(cle_porte)

# TITLE OF CANVAS
pygame.display.set_caption("Rob's quest")
exit = False
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 50)  # add/remove this line

while not exit:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                personnage.move_left()
                personnage.update()
            elif event.key == K_RIGHT:
                personnage.move_right()
                personnage.update()
            elif event.key == K_UP:
                personnage.move_up()
                personnage.update()
            elif event.key == K_DOWN:
                personnage.move_down()
                personnage.update()

        if event.type == KEYUP:
            personnage.image = personnage.images[0]
            personnage.index = 0

    # Clear the window
    screen.fill((255, 255, 255))

    # Draw the player sprite
    screen.blit(personnage.image, personnage.rect)

    pygame.display.update()
