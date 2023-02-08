import pygame
import pytmx
import time
from pygame import *


class GameState():  # source: https://www.youtube.com/watch?v=j9yMFG3D7fg&t=405s
    state = "main_menu"

    def __init__(self, screen):
        self.state = "main_menu"
        self.screen = screen

    def main_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_p:
                    # Lancer le jeu à la place
                    self.state = "level_1"
                if event.key == K_s:
                    # quitter l'jeu
                    exit = True
                    pygame.quit()

        # Affichage sur la fenêtre du menu
        self.screen.blit(image, (250, 200))

        # Bouton Play & Score
        police = pygame.font.SysFont("monospace", 50)
        TextPlay = police.render("'P' = Play", True, (255, 0, 0))
        TextQuit = police.render("'S' = Quitter", True, (255, 0, 0))
        self.screen.blit(TextPlay, (640, 500))
        self.screen.blit(TextQuit, (640, 550))

        # ????
        pygame.display.update()

    def level_final(self, pytmx_map, personnage, objets):
        police = pygame.font.SysFont("monospace", 25)

        # collisions et affichage des tuiles de la map
        layer_index = 0
        for layer in pytmx_map.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = pytmx_map.get_tile_image(x, y, layer_index)
                    if tile != None:
                        self.screen.blit(tile, (x * pytmx_map.tilewidth, y * pytmx_map.tileheight))
                        self.screen.blit(personnage.image, personnage.rect)
            layer_index += 1
            if isinstance(layer, pytmx.TiledObjectGroup):
                if layer.name == "Collisions":
                    for obj in layer:
                        collision = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                        if personnage.rect.colliderect(collision):
                            collide = True
                            dx_correction = (collision.left, collision.right)
                            dy_correction = (collision.top, collision.bottom)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    if not collide:
                        personnage.move_left()
                        personnage.update_left()
                    else:
                        personnage.rect.x += dx_correction[1] - personnage.rect.left

                        collide = False
                elif event.key == K_RIGHT:
                    if not collide:
                        personnage.move_right()
                        personnage.update_right()
                    else:
                        personnage.rect.x += dx_correction[0] - personnage.rect.right

                        collide = False
                elif event.key == K_UP:
                    if not collide:
                        personnage.move_up()
                        personnage.update_back()
                    else:
                        personnage.rect.y += dy_correction[1] - personnage.rect.top

                        collide = False
                elif event.key == K_DOWN:
                    if not collide:
                        personnage.move_down()
                        personnage.update_front()
                    else:
                        personnage.rect.y += dy_correction[0] - personnage.rect.bottom

                        collide = False

            if event.type == KEYUP:
                personnage.image = personnage.images_front[0]  # reprend l'image de la position fixe/statique
                personnage.index = 0


        if personnage.rect.colliderect(objets[0].rect):
            personnage.inventaire.add_item(objets[0])
            objets[0].rect.x = -500  # disparition de l'écran de jeu
            TextPlay = objets[0].notify(police, "+1")
            display_crash_text = True
            start = time.time()

            if not self.screen.get_rect().contains(objets[0].rect):  # si la clé n'est plus dans l'écran de jeu
                objets[0].kill()  # supprime la clé

            # print(personnage.inventaire.get_objects())  # debug

        # Clear the window
        # screen.fill((255, 255, 255))

        self.screen.blit(objets[0].image, objets[0].rect)

        if display_crash_text:
            end = time.time()
            timer = end - start
            if timer > 1.5:
                display_crash_text = False

        self.screen.blit(TextPlay, (400, 400))

    def state_manager(self):
        if self.state == 'main_menu':
            self.main_menu()
        elif self.state == 'level_1':
            self.level_1()

