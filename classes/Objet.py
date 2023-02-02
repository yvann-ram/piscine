import pygame


class Objet(pygame.sprite.Sprite):
    nom = ""
    count = 0
    image = ''
    nom_image = image
    spawn_pos = ()

    def __init__(self, nom, count, image, spawn_pos):
        super(Objet, self).__init__()

        self.nom = nom
        self.count = count
        self.image = pygame.image.load(image).convert_alpha()
        self.nom_image = image
        if spawn_pos != 0:
            self.rect = self.image.get_rect()
            self.rect.x = spawn_pos[0]
            self.rect.y = spawn_pos[1]

    def notify(self, police, state: str):  # notification pop-up sur l'ajout/suppression d'un objet dans l'inventaire
        nom_objet = self.nom

        return police.render(state + " " + nom_objet, True, (0, 0, 0))
