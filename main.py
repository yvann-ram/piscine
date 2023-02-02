import pygame
from pygame import *
# classes
from classes.Personnage import Personnage
from classes.Inventaire import Inventaire
from classes.Objet import Objet

pygame.init()

# CREATING CANVAS
computer_info = pygame.display.Info()  # longueur, largeur de l'écran du PC

screen = pygame.display.set_mode((1280, 720))
cle_porte = Objet("clé de la porte", 1, 'assets/test_cle.png', (600, 600))
cle_coffre = Objet("clé du coffre", 1, 'assets/test_cle.png', 0)
personnage = Personnage((400, 400))

# personnage.inventaire.add_item(cle_porte)
# personnage.inventaire.add_item(cle_coffre)
# personnage.inventaire.remove_item(cle_porte)
# print(personnage.inventaire.get_objects())

# TITLE OF CANVAS
pygame.display.set_caption("Rob's quest")
exit = False
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 50)  # add/remove this line
picked_up_object = False
display_crash_text = False
TextPlay = ""

while not exit:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                personnage.move_left()
                personnage.update()
            if event.key == K_RIGHT:
                personnage.move_right()
                personnage.update()
            if event.key == K_UP:
                personnage.move_up()
                personnage.update()
            if event.key == K_DOWN:
                personnage.move_down()
                personnage.update()

        if event.type == KEYUP:
            personnage.image = personnage.images[0]
            personnage.index = 0

    if personnage.rect.colliderect(cle_porte.rect):
        personnage.inventaire.add_item(cle_porte)
        cle_porte.rect.x = -500
        start_time = pygame.time.get_ticks()
        police = pygame.font.SysFont("monospace", 50)
        TextPlay = police.render("Vous avez obtenu la clé de la porte", True, (255, 0, 0))

        # Check if three seconds have passed. This assumes that "get_current_time()" operates on seconds.
        if pygame.time.get_ticks() - start_time > 3:
            display_crash_text = False

        if not screen.get_rect().contains(cle_porte.rect):
            cle_porte.kill()

        print(personnage.inventaire.get_objects())

    # Clear the window
    screen.fill((255, 255, 255))

    if display_crash_text:
        screen.blit(TextPlay, (400, 400))

    # Draw the player sprite
    screen.blit(personnage.image, personnage.rect)
    screen.blit(cle_porte.image, cle_porte.rect)

    pygame.display.update()
