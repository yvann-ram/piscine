import pygame
from pygame import *

class Gardien(pygame.sprite.Sprite):
    direction = 5.0
    images = []

    def __init__(self):
        super(Gardien, self).__init__()
        self.direction = 5.0
        self.index = 0

        # Définir la position initiale du gardien
        self.character_x = 400
        self.character_y = 300

        self.images.append(pygame.image.load("assets/cop_idle.png").convert_alpha())
        self.images.append(pygame.image.load("assets/cop_run1.png").convert_alpha())
        self.images.append(pygame.image.load("assets/cop_run2.png").convert_alpha())

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

    def set_position(self, pos: []):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    # <editor-fold desc="Animations">
    def update_down(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

    def update_up(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

    # </editor-fold>

    # Faire un aller-retour
    def aller_retour_x(self, depart, arriver):
        self.rect.x += 0.5 * self.direction

        if self.rect.x + self.image.get_width() >= arriver or self.rect.x <= depart:
            self.direction = -self.direction

    def aller_retour_y(self, depart, arriver):
        if self.rect.y <= depart:
            self.direction = 5.0
            self.rect.y += self.direction
            self.update_down()
        elif self.rect.y >= arriver:
            self.direction = -self.direction
            self.rect.y += self.direction
        else:
            self.rect.y += self.direction



