import pygame


class Objet(pygame.sprite.Sprite):
    nom = ""
    count = 0

    def __init__(self, nom, count, image):
        super(Objet, self).__init__()

        self.nom = nom
        self.count = count
        self.image = pygame.image.load(image).convert_alpha()
