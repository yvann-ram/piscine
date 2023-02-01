import pygame


class Objet(pygame.sprite.Sprite):
    nom = ""
    count = 0

    def __init__(self, nom, count):
        super(Objet, self).__init__()

        self.nom = nom
        self.count = count
