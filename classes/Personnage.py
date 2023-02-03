import pygame
from classes.Inventaire import Inventaire
from pygame import mixer
import time

class Personnage(pygame.sprite.Sprite):
    images = []
    inventaire: Inventaire

    def __init__(self, inventaire):
        super(Personnage, self).__init__()
        self.images = []
        self.index = 0
        self.inventaire = inventaire

        self.images.append(pygame.transform.scale(pygame.image.load('assets/playeridle.png').convert_alpha(), (50, 80)))
        self.images.append(pygame.transform.scale(pygame.image.load('assets/playerrun1.png').convert_alpha(), (50, 80)))
        self.images.append(pygame.transform.scale(pygame.image.load('assets/playerrun2.png').convert_alpha(), (50, 80)))
        self.image = self.images[self.index]

        self.rect = self.image.get_rect()

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

    mixer.init()
    mixer.set_num_channels(8)
    pas=mixer.Channel(2)
    foot_sound = mixer.Sound("Sound/Footstep_concrete.wav")
    def bruitdepas(self):
        if not self.pas.get_busy():
            self.pas.play(self.foot_sound)

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

    #Sounds effect
