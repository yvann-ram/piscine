import pygame
from classes.Inventaire import Inventaire
from pygame import mixer


class Personnage(pygame.sprite.Sprite):
    images_left = []
    images_right = []
    images_front = []
    images_back = []
    inventaire: Inventaire = []

    def __init__(self, spawn_pos: []):
        super(Personnage, self).__init__()
        self.images_left = []  # liste des images pour l'animation vers la gauche
        self.images_right = []  # liste des images pour l'animation vers la droite
        self.images_front = []  # liste des images pour l'animation de face
        self.images_back = []  # liste des images pour l'animation de dos
        self.index = 0

        inventaire = Inventaire()
        self.inventaire = inventaire

        # <editor-fold desc="models">

        self.images_left.append(pygame.image.load('assets/rob_idle_left.png').convert_alpha())
        self.images_left.append(pygame.image.load('assets/rob_run_left1.png').convert_alpha())
        self.images_left.append(pygame.image.load('assets/rob_run_left2.png').convert_alpha())

        self.images_right.append(pygame.image.load('assets/rob_idle_right.png').convert_alpha())
        self.images_right.append(pygame.image.load('assets/rob_run_right1.png').convert_alpha())
        self.images_right.append(pygame.image.load('assets/rob_run_right2.png').convert_alpha())

        self.images_front.append(pygame.image.load('assets/rob_idle_front.png').convert_alpha())
        self.images_front.append(pygame.image.load('assets/rob_run_front1.png').convert_alpha())
        self.images_front.append(pygame.image.load('assets/rob_run_front2.png').convert_alpha())

        self.images_back.append(pygame.image.load('assets/rob_idle_back.png').convert_alpha())
        self.images_back.append(pygame.image.load('assets/rob_run_back1.png').convert_alpha())
        self.images_back.append(pygame.image.load('assets/rob_run_back2.png').convert_alpha())

        # </editor-fold>

        self.image = self.images_front[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = spawn_pos[0]
        self.rect.y = spawn_pos[1]

    def get_position(self):
        return self.rect.x, self.rect.y

    def set_position(self, pos: []):
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        print(self.rect.x, self.rect.y)

    mixer.init()
    mixer.set_num_channels(8)
    pas = mixer.Channel(2)
    foot_sound = mixer.Sound("sound/Footstep_concrete.wav")

    def bruitdepas(self):
        if not self.pas.get_busy():
            self.pas.play(self.foot_sound)

    # <editor-fold desc="Mouvements">

    def update_left(self):
        self.index += 1

        if self.index >= len(self.images_left):
            self.index = 0

        self.image = self.images_left[self.index]

    def update_right(self):
        self.index += 1

        if self.index >= len(self.images_right):
            self.index = 0

        self.image = self.images_right[self.index]

    def update_front(self):
        self.index += 1

        if self.index >= len(self.images_front):
            self.index = 0

        self.image = self.images_front[self.index]

    def update_back(self):
        self.index += 1

        if self.index >= len(self.images_back):
            self.index = 0

        self.image = self.images_back[self.index]

    # </editor-fold>

    # <editor-fold desc="Controllers">

    def move_left(self, speed=5):
        self.rect.x -= speed
        self.bruitdepas()

    def move_right(self, speed=5):
        self.rect.x += speed
        self.bruitdepas()

    def move_up(self, speed=5):
        self.rect.y -= speed
        self.bruitdepas()

    def move_down(self, speed=5):
        self.rect.y += speed
        self.bruitdepas()

    # </editor-fold>
