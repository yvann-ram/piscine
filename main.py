import pygame
from pygame import *
from sys import exit as quit
import time
import pytmx
from pytmx.util_pygame import load_pygame
# classes
from classes.Personnage import Personnage
from classes.Objet import Objet
from classes.Gardien import Gardien

pygame.init()

# CREATING CANVAS
computer_info = pygame.display.Info()  # longueur, largeur de l'écran du PC

min_width, min_height = 1600, 900

screen = pygame.display.set_mode((min_width, min_height))
cle_porte = Objet("clé de la porte", 1, 'assets/test_cle.png', [595, 512])
cle_porte2 = Objet("clé de la porte", 1, 'assets/test_cle.png', [976, 370])
cle_coffre = Objet("clé du coffre", 1, 'assets/test_cle.png', 0)

# GENERAL
pygame.display.set_caption("Rob's quest - Démo")
exit = False
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 50)  # add/remove this line
picked_up_object = False
display_crash_text = False
display_no_key_text = False
TextPlay = ""
collide = False

pytmx_map_1 = load_pygame("assets/map1.tmx")  # pygame.image.load("assets/map3.png")
pytmx_map_2 = load_pygame("assets/map2.tmx")  # pygame.image.load("assets/map3.png")
pytmx_map_final = load_pygame("assets/map3.tmx")  # pygame.image.load("assets/map3.png")
main_menu_image = pygame.image.load("ssets/logoA.png")

police = pygame.font.SysFont("monospace", 25)
start = 0

dx_correction = 0
dy_correction = 0
last_pos_x = 820
last_pos_y = 700

personnage = Personnage([820, 700])
gardien1 = Gardien()
gardien2 = Gardien()
spawned = False

TextMan = "Rob issue d'une famille noble avec deux parents archeologue se voit devenir orphelin après une expedition " \
          "menant à leur disparition. Rob n'a que 13 ans mais il est persuadé de pouvoir retrouver sa famille. " \
          "Pendant 10 ans il s'investit dans l'histoire d'objets historiques qu'il retrouve dans les musées afin de " \
          "retracer le parcours de ses parents et enfin résoudre le mystère de leur disparition. "
TextMan = [*TextMan]
Table_end = False

def typing(text, window):
    spacing = 50
    line = 50
    text_end = False
    index = 0
    while not text_end:
        if index < len(text):
            screen_x = screen.get_width()
            text_img = police.render(text[index], True, "WHITE")
            text_width = text_img.get_width()
            if spacing >= screen_x - 50:
                line += 20
                spacing = 50
            screen.blit(text_img, (spacing, line))
            index += 1
            spacing += text_width
            pygame.display.update()
            time.sleep(0.01)
        else:
            text_img = police.render("appuyer sur espace", True, "WHITE")
            screen.blit(text_img, (800, 800))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    return True

        pygame.display.update()
    return True

class GameState:  # source: https://www.youtube.com/watch?v=j9yMFG3D7fg&t=405s
    state = "main_menu"

    def __init__(self, screen):
        self.state = "main_menu"
        self.screen = screen

    def main_menu(self):
        global Table_end, TextMan, screen

        if not Table_end:
            Table_end = typing(TextMan, screen)
            # time.sleep(8)
        else:
            screen.fill((0, 0, 0))
            pygame.mixer.music.load("sound/Musique_fond.wav")
            pygame.mixer.music.play()

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
                    if event.key == K_2:
                        self.state = "level_2"
                    if event.key == K_f:
                        self.state = "level_final"

            # Affichage sur la fenêtre du menu
            self.screen.blit(main_menu_image, (250, 200))

            # Bouton Play & Score
            police = pygame.font.SysFont("monospace", 50)
            TextPlay = police.render("'P' = Play", True, (255, 0, 0))
            TextQuit = police.render("'S' = Quitter", True, (255, 0, 0))
            self.screen.blit(TextPlay, (640, 500))
            self.screen.blit(TextQuit, (640, 550))

        # ????
        pygame.display.update()

    def level_1(self, pytmx_map, objets):
        global start, display_crash_text, police, collide, TextPlay, dx_correction, dy_correction

        self.collisions(pytmx_map, 'level_2', objets, [1315, 535])

        self.mouvement()

        for objet in objets:
            if objet.spawn_pos != 0:
                if personnage.rect.colliderect(objet.rect):
                    personnage.inventaire.add_item(objet)
                    objet.rect.x = -500  # disparition de l'écran de jeu
                    TextPlay = objet.notify(police, "+1")
                    display_crash_text = True
                    self.start = time.time()

                    if objet and not self.screen.get_rect().contains(objet.rect):  # si la clé n'est plus dans l'écran de jeu
                        objet.kill()  # supprime la clé

            # print(personnage.inventaire.get_objects())  # debug

                if objet:
                    self.screen.blit(objet.image, objet.rect)

        if display_crash_text:
            end = time.time()
            timer = end - self.start
            if timer > 1.5:
                display_crash_text = False

            self.screen.blit(TextPlay, (400, 400))

    def level_2(self, pytmx_map, objets):
        global start, display_crash_text, police, collide, TextPlay, dx_correction, dy_correction, spawned
        if not spawned:
            personnage.set_position([298, 530])
            gardien1.set_position([1002, 535])
            gardien2.set_position([1236, 536])
            spawned = True

        self.collisions(pytmx_map, 'level_final', objets, [1325, 320])

        self.mouvement()

        gardien1.aller_retour_y(535, 720)
        gardien2.aller_retour_y(536, 720)

        for objet in objets:
            if objet.spawn_pos != 0:
                if personnage.rect.colliderect(objet.rect):
                    personnage.inventaire.add_item(objet)
                    objet.rect.x = -500  # disparition de l'écran de jeu
                    TextPlay = objet.notify(police, "+1")
                    display_crash_text = True
                    self.start = time.time()

                    if objet and not self.screen.get_rect().contains(objet.rect):  # si la clé n'est plus dans l'écran de jeu
                        objet.kill()  # supprime la clé

            # print(personnage.inventaire.get_objects())  # debug

                if objet:
                    self.screen.blit(objet.image, objet.rect)

        if display_crash_text:
            end = time.time()
            timer = end - self.start
            if timer > 1.5:
                display_crash_text = False

            self.screen.blit(TextPlay, (400, 400))

    def level_final(self, pytmx_map, objets):
        global start, display_crash_text, police, collide, TextPlay, dx_correction, dy_correction, spawned
        if not spawned:
            personnage.set_position([1085, 700])
            spawned = True

        self.collisions(pytmx_map, '', objets, [])

        self.mouvement()

        for objet in objets:
            if objet.spawn_pos != 0:
                if personnage.rect.colliderect(objet.rect):
                    personnage.inventaire.add_item(objet)
                    objet.rect.x = -500  # disparition de l'écran de jeu
                    TextPlay = objet.notify(police, "+1")
                    display_crash_text = True
                    self.start = time.time()

                    if objet and not self.screen.get_rect().contains(objet.rect):  # si la clé n'est plus dans l'écran de jeu
                        objet.kill()  # supprime la clé

            # print(personnage.inventaire.get_objects())  # debug

            if objet:
                self.screen.blit(objet.image, objet.rect)

        if display_crash_text:
            end = time.time()
            timer = end - self.start
            if timer > 1.5:
                display_crash_text = False

            self.screen.blit(TextPlay, (400, 400))


    def mouvement(self):
        global collide, last_pos_x, last_pos_y

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == KEYDOWN:
                if event.key == K_s:
                    pygame.quit()
                    quit()
                if event.key == K_y:
                    print(personnage.get_position())

                if event.key == K_LEFT:
                    if not collide:
                        last_pos_x = personnage.rect.x
                        personnage.move_left()
                        personnage.update_left()
                    else:
                        collide = False

                elif event.key == K_RIGHT:
                    if not collide:
                        last_pos_x = personnage.rect.x  # dernière position_x connue avant collision
                        personnage.move_right()
                        personnage.update_right()
                    else:
                        collide = False

                elif event.key == K_UP:
                    if not collide:
                        last_pos_y = personnage.rect.y  # dernière position_y connue avant collision
                        personnage.move_up()
                        personnage.update_back()
                    else:
                        collide = False

                elif event.key == K_DOWN:
                    if not collide:
                        last_pos_y = personnage.rect.y
                        personnage.move_down()
                        personnage.update_front()
                    else:
                        collide = False

            if event.type == KEYUP:
                personnage.image = personnage.images_front[0]  # reprend l'image de la position fixe/statique
                personnage.index = 0

    def collisions(self, pytmx_map, next_level: str, objet, denied_position):
        global collide, dx_correction, dy_correction, spawned, display_no_key_text

        # collisions et affichage des tuiles de la map
        layer_index = 0
        for layer in pytmx_map.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = pytmx_map.get_tile_image(x, y, layer_index)
                    if tile != None:
                        self.screen.blit(tile, (x * pytmx_map.tilewidth, y * pytmx_map.tileheight))
                        self.screen.blit(personnage.image, personnage.rect)
                        if self.state == 'level_2':
                            self.screen.blit(gardien1.image, gardien1.rect)
                            self.screen.blit(gardien2.image, gardien2.rect)
            layer_index += 1

            if isinstance(layer, pytmx.TiledObjectGroup):
                if layer.name == 'Lvlup':
                    for obj in layer:
                        collision = pygame.Rect(obj.x, obj.y, obj.width, obj.height)

                        if personnage.rect.colliderect(gardien1.rect):
                            self.state = "level_1"
                            print("perdu !")
                        elif personnage.rect.colliderect(gardien2.rect):
                            self.state = "level_1"
                            print("perdu !")

                        if personnage.rect.colliderect(collision) \
                                and personnage.inventaire.has_object_by_name(objet[0].nom):
                            self.state = next_level
                            personnage.inventaire.remove_item(objet[0])
                            spawned = False
                        elif personnage.rect.colliderect(collision) \
                                and not personnage.inventaire.has_object_by_name(objet[0].nom):

                            if display_no_key_text:
                                end = time.time()
                                timer = end - self.start
                                if timer > 2.0:
                                    display_no_key_text = False

                                # self.screen.blit(police.render("La porte est verrouillé", True, "WHITE"), (800, 800))

                            pygame.mixer.music.load("sound/Door_closing.wav")
                            pygame.mixer.music.play()

                            personnage.set_position(denied_position)

                elif layer.name == "Collisions":
                    for obj in layer:
                        collision = pygame.Rect(obj.x, obj.y, obj.width, obj.height)

                        if personnage.rect.colliderect(collision):
                            collide = True
                            personnage.rect.x = last_pos_x
                            personnage.rect.y = last_pos_y

    # def pickup_objects(self, objets):  # TODO
    #     for objet in objets:
    #         if objet.spawn_pos != 0:
    #             if personnage.rect.colliderect(objet.rect):
    #                 personnage.inventaire.add_item(objet)
    #                 objet.rect.x = -500  # disparition de l'écran de jeu
    #                 TextPlay = objet.notify(police, "+1")
    #                 display_crash_text = True
    #                 self.start = time.time()
    #
    #                 if objet and not self.screen.get_rect().contains(objet.rect):
    #                     # si la clé n'est plus dans l'écran de jeu
    #                     objet.kill()  # supprime la clé

    def state_manager(self):
        if self.state == 'main_menu':
            self.main_menu()
        elif self.state == 'level_1':
            self.level_1(pytmx_map_1, [cle_porte])
        elif self.state == 'level_2':
            self.level_2(pytmx_map_2, [cle_porte2])
        elif self.state == 'level_final':
            self.level_final(pytmx_map_final, [])


game_state = GameState(screen)


while not exit:
    clock.tick(30)  # frame par seconde

    game_state.state_manager()

    pygame.display.update()
