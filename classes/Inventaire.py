import pygame
from classes.Objet import Objet


class Inventaire(object):
    inventaire: [Objet] = []

    def __init__(self):
        self.inventaire = []

    def get_inventory(self):
        return self.inventaire

    def Add(self, objet: Objet):
        try:
            self.inventaire.append(objet)
            print("l'objet " + objet.nom + " a été ajouté à l'inventaire")
        except:
            print("une erreur s'est produite")

    def Remove(self, objet: Objet):
        for obj in self.inventaire:
            print(obj, objet)
