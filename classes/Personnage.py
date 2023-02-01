import pygame
from classes.Inventaire import Inventaire


class Personnage(pygame.sprite.Sprite):
    images = []
    inventaire: Inventaire

    def __init__(self, inventaire, spawn_pos):
        super(Personnage, self).__init__()
        self.images = []
        self.index = 0
        self.inventaire = inventaire

        self.images.append(pygame.transform.scale(pygame.image.load('assets/playeridle.png').convert_alpha(), (50, 80)))
        self.images.append(pygame.transform.scale(pygame.image.load('assets/playerrun1.png').convert_alpha(), (50, 80)))
        self.images.append(pygame.transform.scale(pygame.image.load('assets/playerrun2.png').convert_alpha(), (50, 80)))
        self.image = self.images[self.index]

        self.rect = self.image.get_rect()
        self.rect.x = spawn_pos[0]
        self.rect.y = spawn_pos[1]

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

    # <editor-fold desc="Controllers">

    def move_left(self, speed=5):
        self.rect.x -= speed

    def move_right(self, speed=5):
        self.rect.x += speed

    def move_up(self, speed=5):
        self.rect.y -= speed

    def move_down(self, speed=5):
        self.rect.y += speed

    # </editor-fold>
