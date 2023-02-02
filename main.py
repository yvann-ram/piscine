import pygame
from pygame import *
import time
import pytmx
from pytmx.util_pygame import load_pygame
# classes
from classes.Personnage import Personnage
from classes.Objet import Objet

pygame.init()

# CREATING CANVAS
computer_info = pygame.display.Info()  # longueur, largeur de l'écran du PC

min_width, min_height = 1700, 900

screen = pygame.display.set_mode((min_width, min_height))
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
collide = False

pytmx_map = load_pygame("assets/map3(1).tmx")  # pygame.image.load("assets/map3.png")


police = pygame.font.SysFont("monospace", 25)
start = 0

while not exit:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if not collide:
                    personnage.move_left()
                    personnage.update()
                else:
                    personnage.rect.x += 20
            elif event.key == K_RIGHT:
                if not collide:
                    personnage.move_right()
                    personnage.update()
                else:
                    personnage.rect.x -= 20
            elif event.key == K_UP:
                if not collide:
                    personnage.move_up()
                    personnage.update()
                else:
                    personnage.rect.y += 20
            elif event.key == K_DOWN:
                if not collide:
                    personnage.move_down()
                    personnage.update()
                else:
                    personnage.rect.y -= 20

        if event.type == KEYUP:
            personnage.image = personnage.images[0]
            personnage.index = 0

    if personnage.rect.colliderect(cle_porte.rect):
        personnage.inventaire.add_item(cle_porte)
        cle_porte.rect.x = -500
        TextPlay = cle_porte.notify(police, "+1")
        display_crash_text = True
        start = time.time()

        if not screen.get_rect().contains(cle_porte.rect):
            cle_porte.kill()

        print(personnage.inventaire.get_objects())

    # Clear the window
    screen.fill((255, 255, 255))

    layer_index = 0
    for layer in pytmx_map.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = pytmx_map.get_tile_image(x, y, layer_index)
                if tile != None:
                    screen.blit(tile, (x * pytmx_map.tilewidth, y * pytmx_map.tileheight))
        layer_index += 1
        if isinstance(layer, pytmx.TiledObjectGroup):
            if layer.name == "Collisions":
                for obj in layer:
                    if personnage.rect.colliderect(pygame.Rect(obj.x, obj.y, obj.width, obj.height)):
                        collide = True
                    else:
                        collide = False

    screen.blit(personnage.image, personnage.rect)
    screen.blit(cle_porte.image, cle_porte.rect)

    if display_crash_text:
        end = time.time()
        timer = end - start
        if timer > 1.5:
            display_crash_text = False

        screen.blit(TextPlay, (400, 400))

    pygame.display.update()
